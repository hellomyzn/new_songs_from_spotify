import abc

class NewTrackRepoInterface(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def all(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_name_and_artist(self, name: str, artist: str):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def add(self, data: dict):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def delete_by_name_and_artist(self, name: str, artist: str):
        raise NotImplementedError()
