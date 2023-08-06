from PColorLogging import level_to_names, is_level
from PColorLogging.Drawer.color import ColorMode
from PColorLogging.Drawer.message_manager import _MessageManager
from PColorLogging.Drawer.utils import _read_json_file
from PColorLogging.error import NotFoundLevel

BASE_CHARS = ["-", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "s", "f", "d"]


class Drawer:
    def __init__(self, base_message: str, config=None, file_config=None):
        self._base_message = base_message
        self._message = _MessageManager(base_message)
        if file_config is None:
            self.config = config
        else:
            self.config = _read_json_file(file_config)
        self._draw_message()

    @staticmethod
    def _detect_format_attribute(record_attribute: str, base_format_message: str):
        record_attribute = f"%({record_attribute})"
        index = base_format_message.find(record_attribute)
        if index == -1:
            return record_attribute
        base_index = index + len(record_attribute)
        _len = len(base_format_message)
        while base_index < _len:
            if base_format_message[base_index] in BASE_CHARS:
                record_attribute += base_format_message[base_index]
                base_index += 1
            else:
                break
        return record_attribute

    def _draw_message(self):
        if self.config is not None:
            for item in self.config:
                for _level in item["level"]:
                    if _level not in level_to_names:
                        raise NotFoundLevel(_level)
                    str_level = level_to_names[_level]
                    _temp_message = self._message.get_message(str_level)
                    for key in item["config"]:
                        attribute_maker = self._detect_format_attribute(key, _temp_message)
                        new_attribute_maker = attribute_maker
                        _config = item["config"][key]
                        for _item_config in _config:
                            new_attribute_maker = _item_config + new_attribute_maker + ColorMode.RESET
                        _temp_message = _temp_message.replace(attribute_maker, new_attribute_maker)
                    self._message.set_message(str_level, _temp_message)

    def get_message(self, level=None):
        if level is None:
            return self._base_message
        elif not is_level(level):
            return self._base_message
        else:
            return self._message.get_message(level)

    def set_config(self, config):
        self.config = config
        self._draw_message()
