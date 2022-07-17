"""Entory point"""
import logging

import utils.setting as setting
from utils.logger import SetUpLogging
from controllers.track_controller import TrackController



def main():
    """
        This is entry point
    """
    # TODO: Create command for choise
    
    # Init logger
    SetUpLogging().setup_logging(setting.LOG_CONFIG_PATH)
    track_controller = TrackController()

    # track_controller.add_new_tracks_to_playlist()
    # track_controller.remove_tracks_from_playlist()
    track_controller.show_current_track_from_csv()


if __name__ == "__main__":
    main()
