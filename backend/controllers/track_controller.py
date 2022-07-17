"""Modules"""
import logging

import utils.setting as setting
import utils.helper as helper
from models.Spotify import Spotify
from models.Csv import Csv
from models.GoogleSpreadsheet import GoogleSpreadsheet
from services.SpotifyService import SpotifyService
from services.CsvService import CsvService
from services.GoogleSpreadsheetService import GoogleSpreadsheetService


class TrackController(object):
    def __init__(self):
        self.logger_pro = logging.getLogger('production')
        self.logger_dev = logging.getLogger('develop')
        self.logger_con = logging.getLogger('console')

        self.csv = Csv()
        self.spotify = Spotify()
        self.spotify_service = SpotifyService()
        self.google_spreadsheet = GoogleSpreadsheet()
        self.google_spreadsheet_service = GoogleSpreadsheetService()
        self.csv_service = CsvService()

    def show_current_track_from_csv(self) -> None:
        self.logger_pro.info('Start')
        track_from_spotify = self.spotify_service.get_current_track()
        if track_from_spotify:
            track = CsvService.get_track_by_name_and_artist(self.csv.file_path,
                                                            track_from_spotify[0]['name'],
                                                            track_from_spotify[0]['artist'])
            self.csv_service.show_track(track)
        else:
            print("There is no current track")
        return

    def add_new_tracks_to_playlist(self) -> None:
        all_new_tracks = []
        # Add new tracks by each playlist
        for playlist_id in setting.PLAYLISTS_IDS:
            # Retrieve tracks data from playlist
            tracks = SpotifyService.retrieve_tracks_from_playlist(self.spotify,
                                                                  playlist_id)

            # Retrieve only new tracks
            new_tracks = SpotifyService.retrieve_new_tracks(self.spotify,
                                                            tracks,
                                                            self.csv.file_path)

            # Add tracks to CSV
            CsvService.add_tracks(self.csv, new_tracks)

            # Add new tracks of the playlist to total one
            if new_tracks:
                all_new_tracks += new_tracks

        # Add tracks to google spreadsheet
        GoogleSpreadsheetService.add_tracks(self.google_spreadsheet,
                                            all_new_tracks)

        # Add tracks to a playlist on Spotify
        SpotifyService.add_tracks_to_playlist(self.spotify,
                                              all_new_tracks,
                                              setting.MY_PLAYLIST_ID)

        return

    def remove_tracks_from_playlist(self) -> None:
        question = "\nDo you want to remove some tracks you've already listened from playlist? (y/n): "
        if helper.is_yes(input(question)):
            SpotifyService.remove_tracks_played_recently_from_playlist(self.spotify,
                                                                       setting.MY_PLAYLIST_ID)
        else:
            print('You can remove tracks between the track number(first) you choose and the track number(last) you choose')
            first = int(input('Enter a track number (first): '))
            last = int(input('Enter a track number (last): '))
            SpotifyService.remove_tracks_from_playlist(self.spotify,
                                                       setting.MY_PLAYLIST_ID, first,
                                                       last)
        return
