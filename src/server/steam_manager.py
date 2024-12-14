#come back once base game working

from ctypes import c_void_p, c_char_p, c_uint32, c_int32, c_int, byref, Structure, POINTER
from steamworks_wrapper.steamworks_bindings import steam_lib

class SteamParamStringArray_t(Structure):
    _fields_ = [
        ("m_ppStrings", POINTER(c_char_p)),
        ("m_nNumStrings", c_int),
    ]

class SteamManager:
    def __init__(self):
        # Initialize Steamworks API
        pass
        

        
    def publish_workshop_file(self, file_path, preview_path, app_id, title, description, visibility, tags, file_type):
        if not steam_lib.SteamAPI_InitFlat():
            raise RuntimeError("Failed to initialize Steamworks API")
        print("Steamworks API initialized.")
        steamRemoteStorage = steam_lib.SteamAPI_SteamRemoteStorage_v016()
        if not steamRemoteStorage:
            print("SteamAPI_SteamRemoteStorage_v016 returned NULL.")
            raise RuntimeError("Failed to obtain ISteamRemoteStorage interface")
        print(f"SteamRemoteStorage interface: {steamRemoteStorage}")
        # Prepare tags
        tag_array = (c_char_p * len(tags))(*[c_char_p(tag.encode()) for tag in tags])
        steam_tags = SteamParamStringArray_t(m_ppStrings=tag_array, m_nNumStrings=len(tags))

        # Call PublishWorkshopFile
        result = steam_lib.SteamAPI_ISteamRemoteStorage_PublishWorkshopFile(
            steamRemoteStorage,
            c_char_p(file_path.encode()),
            c_char_p(preview_path.encode()),
            c_int32(app_id),
            c_char_p(title.encode()),
            c_char_p(description.encode()),
            c_int(visibility),
            byref(steam_tags),
            c_int(file_type),
        )
        return result


