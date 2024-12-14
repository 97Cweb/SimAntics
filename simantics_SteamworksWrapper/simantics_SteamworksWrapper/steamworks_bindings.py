import ctypes

import platform

import os

# Dynamically locate the Steamworks library

redistributable_bin_path = {

    'Windows': {

        '64bit': r'steamworks_sdk_161/sdk/redistributable_bin/win64/steam_api64.dll',

        '32bit': r'steamworks_sdk_161/sdk/redistributable_bin/steam_api.dll'

    },

    'Linux': {

        '64bit': r'steamworks_sdk_161/sdk/redistributable_bin/linux64/libsteam_api.so',

        '32bit': r'steamworks_sdk_161/sdk/redistributable_bin/linux32/libsteam_api.so'

    }

}


system = platform.system()
architecture = platform.architecture()[0]
if system not in redistributable_bin_path or architecture not in redistributable_bin_path[system]:
    raise OSError(f'Unsupported platform or architecture: {system} {architecture}')
library_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), redistributable_bin_path[system][architecture])
if not os.path.exists(library_path):
    raise FileNotFoundError(f'Steamworks library not found: {library_path}')
steam_lib = ctypes.CDLL(library_path)


# Binding for SteamAPI_ISteamClient_CreateSteamPipe

steam_lib.SteamAPI_ISteamClient_CreateSteamPipe.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_CreateSteamPipe.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_BReleaseSteamPipe

steam_lib.SteamAPI_ISteamClient_BReleaseSteamPipe.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamClient_BReleaseSteamPipe.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_ConnectToGlobalUser

steam_lib.SteamAPI_ISteamClient_ConnectToGlobalUser.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamClient_ConnectToGlobalUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_CreateLocalUser

steam_lib.SteamAPI_ISteamClient_CreateLocalUser.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamClient_CreateLocalUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_ReleaseUser

steam_lib.SteamAPI_ISteamClient_ReleaseUser.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamClient_ReleaseUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamUser

steam_lib.SteamAPI_ISteamClient_GetISteamUser.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamGameServer

steam_lib.SteamAPI_ISteamClient_GetISteamGameServer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamGameServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_SetLocalIPBinding

steam_lib.SteamAPI_ISteamClient_SetLocalIPBinding.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamClient_SetLocalIPBinding.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamFriends

steam_lib.SteamAPI_ISteamClient_GetISteamFriends.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamFriends.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamUtils

steam_lib.SteamAPI_ISteamClient_GetISteamUtils.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamUtils.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamMatchmaking

steam_lib.SteamAPI_ISteamClient_GetISteamMatchmaking.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamMatchmaking.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamMatchmakingServers

steam_lib.SteamAPI_ISteamClient_GetISteamMatchmakingServers.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamMatchmakingServers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamGenericInterface

steam_lib.SteamAPI_ISteamClient_GetISteamGenericInterface.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamGenericInterface.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamUserStats

steam_lib.SteamAPI_ISteamClient_GetISteamUserStats.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamUserStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamGameServerStats

steam_lib.SteamAPI_ISteamClient_GetISteamGameServerStats.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamGameServerStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamApps

steam_lib.SteamAPI_ISteamClient_GetISteamApps.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamApps.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamNetworking

steam_lib.SteamAPI_ISteamClient_GetISteamNetworking.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamNetworking.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamRemoteStorage

steam_lib.SteamAPI_ISteamClient_GetISteamRemoteStorage.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamRemoteStorage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamScreenshots

steam_lib.SteamAPI_ISteamClient_GetISteamScreenshots.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamScreenshots.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamGameSearch

steam_lib.SteamAPI_ISteamClient_GetISteamGameSearch.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamGameSearch.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetIPCCallCount

steam_lib.SteamAPI_ISteamClient_GetIPCCallCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetIPCCallCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_SetWarningMessageHook

steam_lib.SteamAPI_ISteamClient_SetWarningMessageHook.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamClient_SetWarningMessageHook.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_BShutdownIfAllPipesClosed

steam_lib.SteamAPI_ISteamClient_BShutdownIfAllPipesClosed.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_BShutdownIfAllPipesClosed.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamHTTP

steam_lib.SteamAPI_ISteamClient_GetISteamHTTP.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamHTTP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamController

steam_lib.SteamAPI_ISteamClient_GetISteamController.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamController.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamUGC

steam_lib.SteamAPI_ISteamClient_GetISteamUGC.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamUGC.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamMusic

steam_lib.SteamAPI_ISteamClient_GetISteamMusic.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamMusic.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamMusicRemote

steam_lib.SteamAPI_ISteamClient_GetISteamMusicRemote.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamMusicRemote.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamHTMLSurface

steam_lib.SteamAPI_ISteamClient_GetISteamHTMLSurface.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamHTMLSurface.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamInventory

steam_lib.SteamAPI_ISteamClient_GetISteamInventory.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamInventory.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamVideo

steam_lib.SteamAPI_ISteamClient_GetISteamVideo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamVideo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamParentalSettings

steam_lib.SteamAPI_ISteamClient_GetISteamParentalSettings.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamParentalSettings.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamInput

steam_lib.SteamAPI_ISteamClient_GetISteamInput.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamInput.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamParties

steam_lib.SteamAPI_ISteamClient_GetISteamParties.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamParties.restype = ctypes.c_int


# Binding for SteamAPI_ISteamClient_GetISteamRemotePlay

steam_lib.SteamAPI_ISteamClient_GetISteamRemotePlay.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamClient_GetISteamRemotePlay.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetHSteamUser

steam_lib.SteamAPI_ISteamUser_GetHSteamUser.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetHSteamUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_BLoggedOn

steam_lib.SteamAPI_ISteamUser_BLoggedOn.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_BLoggedOn.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetSteamID

steam_lib.SteamAPI_ISteamUser_GetSteamID.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetSteamID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_InitiateGameConnection_DEPRECATED

steam_lib.SteamAPI_ISteamUser_InitiateGameConnection_DEPRECATED.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_InitiateGameConnection_DEPRECATED.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_TerminateGameConnection_DEPRECATED

steam_lib.SteamAPI_ISteamUser_TerminateGameConnection_DEPRECATED.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_TerminateGameConnection_DEPRECATED.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_TrackAppUsageEvent

steam_lib.SteamAPI_ISteamUser_TrackAppUsageEvent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_TrackAppUsageEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetUserDataFolder

steam_lib.SteamAPI_ISteamUser_GetUserDataFolder.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_GetUserDataFolder.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_StartVoiceRecording

steam_lib.SteamAPI_ISteamUser_StartVoiceRecording.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_StartVoiceRecording.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_StopVoiceRecording

steam_lib.SteamAPI_ISteamUser_StopVoiceRecording.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_StopVoiceRecording.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetAvailableVoice

steam_lib.SteamAPI_ISteamUser_GetAvailableVoice.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_GetAvailableVoice.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetVoice

steam_lib.SteamAPI_ISteamUser_GetVoice.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_GetVoice.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_DecompressVoice

steam_lib.SteamAPI_ISteamUser_DecompressVoice.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_DecompressVoice.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetVoiceOptimalSampleRate

steam_lib.SteamAPI_ISteamUser_GetVoiceOptimalSampleRate.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetVoiceOptimalSampleRate.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetAuthSessionTicket

steam_lib.SteamAPI_ISteamUser_GetAuthSessionTicket.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetAuthSessionTicket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetAuthTicketForWebApi

steam_lib.SteamAPI_ISteamUser_GetAuthTicketForWebApi.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetAuthTicketForWebApi.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_BeginAuthSession

steam_lib.SteamAPI_ISteamUser_BeginAuthSession.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_BeginAuthSession.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_EndAuthSession

steam_lib.SteamAPI_ISteamUser_EndAuthSession.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_EndAuthSession.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_CancelAuthTicket

steam_lib.SteamAPI_ISteamUser_CancelAuthTicket.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_CancelAuthTicket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_UserHasLicenseForApp

steam_lib.SteamAPI_ISteamUser_UserHasLicenseForApp.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_UserHasLicenseForApp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_BIsBehindNAT

steam_lib.SteamAPI_ISteamUser_BIsBehindNAT.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_BIsBehindNAT.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_AdvertiseGame

steam_lib.SteamAPI_ISteamUser_AdvertiseGame.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_AdvertiseGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_RequestEncryptedAppTicket

steam_lib.SteamAPI_ISteamUser_RequestEncryptedAppTicket.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_RequestEncryptedAppTicket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetEncryptedAppTicket

steam_lib.SteamAPI_ISteamUser_GetEncryptedAppTicket.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetEncryptedAppTicket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetGameBadgeLevel

steam_lib.SteamAPI_ISteamUser_GetGameBadgeLevel.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_GetGameBadgeLevel.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetPlayerSteamLevel

steam_lib.SteamAPI_ISteamUser_GetPlayerSteamLevel.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetPlayerSteamLevel.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_RequestStoreAuthURL

steam_lib.SteamAPI_ISteamUser_RequestStoreAuthURL.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_RequestStoreAuthURL.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_BIsPhoneVerified

steam_lib.SteamAPI_ISteamUser_BIsPhoneVerified.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_BIsPhoneVerified.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_BIsTwoFactorEnabled

steam_lib.SteamAPI_ISteamUser_BIsTwoFactorEnabled.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_BIsTwoFactorEnabled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_BIsPhoneIdentifying

steam_lib.SteamAPI_ISteamUser_BIsPhoneIdentifying.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_BIsPhoneIdentifying.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_BIsPhoneRequiringVerification

steam_lib.SteamAPI_ISteamUser_BIsPhoneRequiringVerification.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_BIsPhoneRequiringVerification.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetMarketEligibility

steam_lib.SteamAPI_ISteamUser_GetMarketEligibility.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetMarketEligibility.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_GetDurationControl

steam_lib.SteamAPI_ISteamUser_GetDurationControl.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUser_GetDurationControl.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUser_BSetDurationControlOnlineState

steam_lib.SteamAPI_ISteamUser_BSetDurationControlOnlineState.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUser_BSetDurationControlOnlineState.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetPersonaName

steam_lib.SteamAPI_ISteamFriends_GetPersonaName.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetPersonaName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_SetPersonaName

steam_lib.SteamAPI_ISteamFriends_SetPersonaName.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_SetPersonaName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetPersonaState

steam_lib.SteamAPI_ISteamFriends_GetPersonaState.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetPersonaState.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendCount

steam_lib.SteamAPI_ISteamFriends_GetFriendCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendByIndex

steam_lib.SteamAPI_ISteamFriends_GetFriendByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendRelationship

steam_lib.SteamAPI_ISteamFriends_GetFriendRelationship.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendRelationship.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendPersonaState

steam_lib.SteamAPI_ISteamFriends_GetFriendPersonaState.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendPersonaState.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendPersonaName

steam_lib.SteamAPI_ISteamFriends_GetFriendPersonaName.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendPersonaName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendGamePlayed

steam_lib.SteamAPI_ISteamFriends_GetFriendGamePlayed.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetFriendGamePlayed.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendPersonaNameHistory

steam_lib.SteamAPI_ISteamFriends_GetFriendPersonaNameHistory.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendPersonaNameHistory.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendSteamLevel

steam_lib.SteamAPI_ISteamFriends_GetFriendSteamLevel.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendSteamLevel.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetPlayerNickname

steam_lib.SteamAPI_ISteamFriends_GetPlayerNickname.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetPlayerNickname.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendsGroupCount

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendsGroupIDByIndex

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupIDByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupIDByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendsGroupName

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupName.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendsGroupMembersCount

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupMembersCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupMembersCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendsGroupMembersList

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupMembersList.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendsGroupMembersList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_HasFriend

steam_lib.SteamAPI_ISteamFriends_HasFriend.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_HasFriend.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanCount

steam_lib.SteamAPI_ISteamFriends_GetClanCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetClanCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanByIndex

steam_lib.SteamAPI_ISteamFriends_GetClanByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetClanByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanName

steam_lib.SteamAPI_ISteamFriends_GetClanName.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetClanName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanTag

steam_lib.SteamAPI_ISteamFriends_GetClanTag.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetClanTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanActivityCounts

steam_lib.SteamAPI_ISteamFriends_GetClanActivityCounts.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetClanActivityCounts.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_DownloadClanActivityCounts

steam_lib.SteamAPI_ISteamFriends_DownloadClanActivityCounts.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_DownloadClanActivityCounts.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendCountFromSource

steam_lib.SteamAPI_ISteamFriends_GetFriendCountFromSource.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendCountFromSource.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendFromSourceByIndex

steam_lib.SteamAPI_ISteamFriends_GetFriendFromSourceByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendFromSourceByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_IsUserInSource

steam_lib.SteamAPI_ISteamFriends_IsUserInSource.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_IsUserInSource.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_SetInGameVoiceSpeaking

steam_lib.SteamAPI_ISteamFriends_SetInGameVoiceSpeaking.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_SetInGameVoiceSpeaking.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ActivateGameOverlay

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlay.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlay.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ActivateGameOverlayToUser

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayToUser.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayToUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ActivateGameOverlayToWebPage

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayToWebPage.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayToWebPage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ActivateGameOverlayToStore

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayToStore.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayToStore.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_SetPlayedWith

steam_lib.SteamAPI_ISteamFriends_SetPlayedWith.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_SetPlayedWith.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialog

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialog.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialog.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetSmallFriendAvatar

steam_lib.SteamAPI_ISteamFriends_GetSmallFriendAvatar.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetSmallFriendAvatar.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetMediumFriendAvatar

steam_lib.SteamAPI_ISteamFriends_GetMediumFriendAvatar.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetMediumFriendAvatar.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetLargeFriendAvatar

steam_lib.SteamAPI_ISteamFriends_GetLargeFriendAvatar.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetLargeFriendAvatar.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_RequestUserInformation

steam_lib.SteamAPI_ISteamFriends_RequestUserInformation.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_RequestUserInformation.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_RequestClanOfficerList

steam_lib.SteamAPI_ISteamFriends_RequestClanOfficerList.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_RequestClanOfficerList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanOwner

steam_lib.SteamAPI_ISteamFriends_GetClanOwner.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetClanOwner.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanOfficerCount

steam_lib.SteamAPI_ISteamFriends_GetClanOfficerCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetClanOfficerCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanOfficerByIndex

steam_lib.SteamAPI_ISteamFriends_GetClanOfficerByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetClanOfficerByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetUserRestrictions

steam_lib.SteamAPI_ISteamFriends_GetUserRestrictions.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetUserRestrictions.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_SetRichPresence

steam_lib.SteamAPI_ISteamFriends_SetRichPresence.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_SetRichPresence.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ClearRichPresence

steam_lib.SteamAPI_ISteamFriends_ClearRichPresence.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_ClearRichPresence.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendRichPresence

steam_lib.SteamAPI_ISteamFriends_GetFriendRichPresence.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetFriendRichPresence.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendRichPresenceKeyCount

steam_lib.SteamAPI_ISteamFriends_GetFriendRichPresenceKeyCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendRichPresenceKeyCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendRichPresenceKeyByIndex

steam_lib.SteamAPI_ISteamFriends_GetFriendRichPresenceKeyByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendRichPresenceKeyByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_RequestFriendRichPresence

steam_lib.SteamAPI_ISteamFriends_RequestFriendRichPresence.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_RequestFriendRichPresence.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_InviteUserToGame

steam_lib.SteamAPI_ISteamFriends_InviteUserToGame.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_InviteUserToGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetCoplayFriendCount

steam_lib.SteamAPI_ISteamFriends_GetCoplayFriendCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetCoplayFriendCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetCoplayFriend

steam_lib.SteamAPI_ISteamFriends_GetCoplayFriend.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetCoplayFriend.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendCoplayTime

steam_lib.SteamAPI_ISteamFriends_GetFriendCoplayTime.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendCoplayTime.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendCoplayGame

steam_lib.SteamAPI_ISteamFriends_GetFriendCoplayGame.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFriendCoplayGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_JoinClanChatRoom

steam_lib.SteamAPI_ISteamFriends_JoinClanChatRoom.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_JoinClanChatRoom.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_LeaveClanChatRoom

steam_lib.SteamAPI_ISteamFriends_LeaveClanChatRoom.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_LeaveClanChatRoom.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanChatMemberCount

steam_lib.SteamAPI_ISteamFriends_GetClanChatMemberCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetClanChatMemberCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetChatMemberByIndex

steam_lib.SteamAPI_ISteamFriends_GetChatMemberByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetChatMemberByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_SendClanChatMessage

steam_lib.SteamAPI_ISteamFriends_SendClanChatMessage.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_SendClanChatMessage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetClanChatMessage

steam_lib.SteamAPI_ISteamFriends_GetClanChatMessage.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetClanChatMessage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_IsClanChatAdmin

steam_lib.SteamAPI_ISteamFriends_IsClanChatAdmin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_IsClanChatAdmin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_IsClanChatWindowOpenInSteam

steam_lib.SteamAPI_ISteamFriends_IsClanChatWindowOpenInSteam.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_IsClanChatWindowOpenInSteam.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_OpenClanChatWindowInSteam

steam_lib.SteamAPI_ISteamFriends_OpenClanChatWindowInSteam.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_OpenClanChatWindowInSteam.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_CloseClanChatWindowInSteam

steam_lib.SteamAPI_ISteamFriends_CloseClanChatWindowInSteam.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_CloseClanChatWindowInSteam.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_SetListenForFriendsMessages

steam_lib.SteamAPI_ISteamFriends_SetListenForFriendsMessages.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_SetListenForFriendsMessages.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ReplyToFriendMessage

steam_lib.SteamAPI_ISteamFriends_ReplyToFriendMessage.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_ReplyToFriendMessage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFriendMessage

steam_lib.SteamAPI_ISteamFriends_GetFriendMessage.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetFriendMessage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetFollowerCount

steam_lib.SteamAPI_ISteamFriends_GetFollowerCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetFollowerCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_IsFollowing

steam_lib.SteamAPI_ISteamFriends_IsFollowing.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_IsFollowing.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_EnumerateFollowingList

steam_lib.SteamAPI_ISteamFriends_EnumerateFollowingList.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_EnumerateFollowingList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_IsClanPublic

steam_lib.SteamAPI_ISteamFriends_IsClanPublic.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_IsClanPublic.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_IsClanOfficialGameGroup

steam_lib.SteamAPI_ISteamFriends_IsClanOfficialGameGroup.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_IsClanOfficialGameGroup.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetNumChatsWithUnreadPriorityMessages

steam_lib.SteamAPI_ISteamFriends_GetNumChatsWithUnreadPriorityMessages.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_GetNumChatsWithUnreadPriorityMessages.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayRemotePlayTogetherInviteDialog.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_RegisterProtocolInOverlayBrowser

steam_lib.SteamAPI_ISteamFriends_RegisterProtocolInOverlayBrowser.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_RegisterProtocolInOverlayBrowser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialogConnectString

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialogConnectString.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamFriends_ActivateGameOverlayInviteDialogConnectString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_RequestEquippedProfileItems

steam_lib.SteamAPI_ISteamFriends_RequestEquippedProfileItems.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_RequestEquippedProfileItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_BHasEquippedProfileItem

steam_lib.SteamAPI_ISteamFriends_BHasEquippedProfileItem.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_BHasEquippedProfileItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetProfileItemPropertyString

steam_lib.SteamAPI_ISteamFriends_GetProfileItemPropertyString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetProfileItemPropertyString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamFriends_GetProfileItemPropertyUint

steam_lib.SteamAPI_ISteamFriends_GetProfileItemPropertyUint.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamFriends_GetProfileItemPropertyUint.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetSecondsSinceAppActive

steam_lib.SteamAPI_ISteamUtils_GetSecondsSinceAppActive.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetSecondsSinceAppActive.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetSecondsSinceComputerActive

steam_lib.SteamAPI_ISteamUtils_GetSecondsSinceComputerActive.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetSecondsSinceComputerActive.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetConnectedUniverse

steam_lib.SteamAPI_ISteamUtils_GetConnectedUniverse.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetConnectedUniverse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetServerRealTime

steam_lib.SteamAPI_ISteamUtils_GetServerRealTime.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetServerRealTime.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetIPCountry

steam_lib.SteamAPI_ISteamUtils_GetIPCountry.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetIPCountry.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetImageSize

steam_lib.SteamAPI_ISteamUtils_GetImageSize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetImageSize.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetImageRGBA

steam_lib.SteamAPI_ISteamUtils_GetImageRGBA.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_GetImageRGBA.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetCurrentBatteryPower

steam_lib.SteamAPI_ISteamUtils_GetCurrentBatteryPower.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetCurrentBatteryPower.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetAppID

steam_lib.SteamAPI_ISteamUtils_GetAppID.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetAppID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_SetOverlayNotificationPosition

steam_lib.SteamAPI_ISteamUtils_SetOverlayNotificationPosition.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_SetOverlayNotificationPosition.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_IsAPICallCompleted

steam_lib.SteamAPI_ISteamUtils_IsAPICallCompleted.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_IsAPICallCompleted.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetAPICallFailureReason

steam_lib.SteamAPI_ISteamUtils_GetAPICallFailureReason.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_GetAPICallFailureReason.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetAPICallResult

steam_lib.SteamAPI_ISteamUtils_GetAPICallResult.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetAPICallResult.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetIPCCallCount

steam_lib.SteamAPI_ISteamUtils_GetIPCCallCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetIPCCallCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_SetWarningMessageHook

steam_lib.SteamAPI_ISteamUtils_SetWarningMessageHook.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_SetWarningMessageHook.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_IsOverlayEnabled

steam_lib.SteamAPI_ISteamUtils_IsOverlayEnabled.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_IsOverlayEnabled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_BOverlayNeedsPresent

steam_lib.SteamAPI_ISteamUtils_BOverlayNeedsPresent.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_BOverlayNeedsPresent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_CheckFileSignature

steam_lib.SteamAPI_ISteamUtils_CheckFileSignature.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_CheckFileSignature.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_ShowGamepadTextInput

steam_lib.SteamAPI_ISteamUtils_ShowGamepadTextInput.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_ShowGamepadTextInput.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetEnteredGamepadTextLength

steam_lib.SteamAPI_ISteamUtils_GetEnteredGamepadTextLength.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetEnteredGamepadTextLength.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetEnteredGamepadTextInput

steam_lib.SteamAPI_ISteamUtils_GetEnteredGamepadTextInput.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_GetEnteredGamepadTextInput.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetSteamUILanguage

steam_lib.SteamAPI_ISteamUtils_GetSteamUILanguage.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_GetSteamUILanguage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_IsSteamRunningInVR

steam_lib.SteamAPI_ISteamUtils_IsSteamRunningInVR.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_IsSteamRunningInVR.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_SetOverlayNotificationInset

steam_lib.SteamAPI_ISteamUtils_SetOverlayNotificationInset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_SetOverlayNotificationInset.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_IsSteamInBigPictureMode

steam_lib.SteamAPI_ISteamUtils_IsSteamInBigPictureMode.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_IsSteamInBigPictureMode.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_StartVRDashboard

steam_lib.SteamAPI_ISteamUtils_StartVRDashboard.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_StartVRDashboard.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_IsVRHeadsetStreamingEnabled

steam_lib.SteamAPI_ISteamUtils_IsVRHeadsetStreamingEnabled.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_IsVRHeadsetStreamingEnabled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_SetVRHeadsetStreamingEnabled

steam_lib.SteamAPI_ISteamUtils_SetVRHeadsetStreamingEnabled.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_SetVRHeadsetStreamingEnabled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_IsSteamChinaLauncher

steam_lib.SteamAPI_ISteamUtils_IsSteamChinaLauncher.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_IsSteamChinaLauncher.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_InitFilterText

steam_lib.SteamAPI_ISteamUtils_InitFilterText.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_InitFilterText.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_FilterText

steam_lib.SteamAPI_ISteamUtils_FilterText.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_FilterText.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_GetIPv6ConnectivityState

steam_lib.SteamAPI_ISteamUtils_GetIPv6ConnectivityState.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_GetIPv6ConnectivityState.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_IsSteamRunningOnSteamDeck

steam_lib.SteamAPI_ISteamUtils_IsSteamRunningOnSteamDeck.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_IsSteamRunningOnSteamDeck.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_ShowFloatingGamepadTextInput

steam_lib.SteamAPI_ISteamUtils_ShowFloatingGamepadTextInput.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_ShowFloatingGamepadTextInput.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_SetGameLauncherMode

steam_lib.SteamAPI_ISteamUtils_SetGameLauncherMode.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUtils_SetGameLauncherMode.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_DismissFloatingGamepadTextInput

steam_lib.SteamAPI_ISteamUtils_DismissFloatingGamepadTextInput.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_DismissFloatingGamepadTextInput.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUtils_DismissGamepadTextInput

steam_lib.SteamAPI_ISteamUtils_DismissGamepadTextInput.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUtils_DismissGamepadTextInput.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetFavoriteGameCount

steam_lib.SteamAPI_ISteamMatchmaking_GetFavoriteGameCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_GetFavoriteGameCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetFavoriteGame

steam_lib.SteamAPI_ISteamMatchmaking_GetFavoriteGame.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_GetFavoriteGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_AddFavoriteGame

steam_lib.SteamAPI_ISteamMatchmaking_AddFavoriteGame.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_AddFavoriteGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_RemoveFavoriteGame

steam_lib.SteamAPI_ISteamMatchmaking_RemoveFavoriteGame.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_RemoveFavoriteGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_RequestLobbyList

steam_lib.SteamAPI_ISteamMatchmaking_RequestLobbyList.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_RequestLobbyList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_AddRequestLobbyListStringFilter

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListStringFilter.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListStringFilter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_AddRequestLobbyListNumericalFilter

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListNumericalFilter.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListNumericalFilter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_AddRequestLobbyListNearValueFilter

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListNearValueFilter.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListNearValueFilter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListFilterSlotsAvailable.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_AddRequestLobbyListDistanceFilter

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListDistanceFilter.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListDistanceFilter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_AddRequestLobbyListResultCountFilter

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListResultCountFilter.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListResultCountFilter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_AddRequestLobbyListCompatibleMembersFilter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyByIndex

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_CreateLobby

steam_lib.SteamAPI_ISteamMatchmaking_CreateLobby.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_CreateLobby.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_JoinLobby

steam_lib.SteamAPI_ISteamMatchmaking_JoinLobby.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_JoinLobby.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_LeaveLobby

steam_lib.SteamAPI_ISteamMatchmaking_LeaveLobby.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_LeaveLobby.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_InviteUserToLobby

steam_lib.SteamAPI_ISteamMatchmaking_InviteUserToLobby.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_InviteUserToLobby.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetNumLobbyMembers

steam_lib.SteamAPI_ISteamMatchmaking_GetNumLobbyMembers.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_GetNumLobbyMembers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyMemberByIndex

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyMemberByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyMemberByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyData

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SetLobbyData

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyDataCount

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyDataCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyDataCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyDataByIndex

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyDataByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyDataByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_DeleteLobbyData

steam_lib.SteamAPI_ISteamMatchmaking_DeleteLobbyData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_DeleteLobbyData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyMemberData

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyMemberData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyMemberData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SetLobbyMemberData

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyMemberData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyMemberData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SendLobbyChatMsg

steam_lib.SteamAPI_ISteamMatchmaking_SendLobbyChatMsg.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_SendLobbyChatMsg.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyChatEntry

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyChatEntry.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyChatEntry.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_RequestLobbyData

steam_lib.SteamAPI_ISteamMatchmaking_RequestLobbyData.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_RequestLobbyData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SetLobbyGameServer

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyGameServer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyGameServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyGameServer

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyGameServer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyGameServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SetLobbyMemberLimit

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyMemberLimit.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyMemberLimit.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyMemberLimit

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyMemberLimit.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyMemberLimit.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SetLobbyType

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyType.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyType.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SetLobbyJoinable

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyJoinable.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyJoinable.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_GetLobbyOwner

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyOwner.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_GetLobbyOwner.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SetLobbyOwner

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyOwner.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_SetLobbyOwner.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmaking_SetLinkedLobby

steam_lib.SteamAPI_ISteamMatchmaking_SetLinkedLobby.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmaking_SetLinkedLobby.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServerListResponse_ServerResponded

steam_lib.SteamAPI_ISteamMatchmakingServerListResponse_ServerResponded.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServerListResponse_ServerResponded.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServerListResponse_ServerFailedToRespond

steam_lib.SteamAPI_ISteamMatchmakingServerListResponse_ServerFailedToRespond.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServerListResponse_ServerFailedToRespond.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServerListResponse_RefreshComplete

steam_lib.SteamAPI_ISteamMatchmakingServerListResponse_RefreshComplete.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServerListResponse_RefreshComplete.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingPingResponse_ServerResponded

steam_lib.SteamAPI_ISteamMatchmakingPingResponse_ServerResponded.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingPingResponse_ServerResponded.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingPingResponse_ServerFailedToRespond

steam_lib.SteamAPI_ISteamMatchmakingPingResponse_ServerFailedToRespond.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingPingResponse_ServerFailedToRespond.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingPlayersResponse_AddPlayerToList

steam_lib.SteamAPI_ISteamMatchmakingPlayersResponse_AddPlayerToList.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingPlayersResponse_AddPlayerToList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingPlayersResponse_PlayersFailedToRespond

steam_lib.SteamAPI_ISteamMatchmakingPlayersResponse_PlayersFailedToRespond.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingPlayersResponse_PlayersFailedToRespond.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingPlayersResponse_PlayersRefreshComplete

steam_lib.SteamAPI_ISteamMatchmakingPlayersResponse_PlayersRefreshComplete.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingPlayersResponse_PlayersRefreshComplete.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingRulesResponse_RulesResponded

steam_lib.SteamAPI_ISteamMatchmakingRulesResponse_RulesResponded.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingRulesResponse_RulesResponded.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingRulesResponse_RulesFailedToRespond

steam_lib.SteamAPI_ISteamMatchmakingRulesResponse_RulesFailedToRespond.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingRulesResponse_RulesFailedToRespond.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingRulesResponse_RulesRefreshComplete

steam_lib.SteamAPI_ISteamMatchmakingRulesResponse_RulesRefreshComplete.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingRulesResponse_RulesRefreshComplete.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_RequestInternetServerList

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestInternetServerList.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestInternetServerList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_RequestLANServerList

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestLANServerList.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestLANServerList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_RequestFriendsServerList

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestFriendsServerList.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestFriendsServerList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_RequestFavoritesServerList

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestFavoritesServerList.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestFavoritesServerList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_RequestHistoryServerList

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestHistoryServerList.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestHistoryServerList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_RequestSpectatorServerList

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestSpectatorServerList.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_RequestSpectatorServerList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_ReleaseRequest

steam_lib.SteamAPI_ISteamMatchmakingServers_ReleaseRequest.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServers_ReleaseRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_GetServerDetails

steam_lib.SteamAPI_ISteamMatchmakingServers_GetServerDetails.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServers_GetServerDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_CancelQuery

steam_lib.SteamAPI_ISteamMatchmakingServers_CancelQuery.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServers_CancelQuery.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_RefreshQuery

steam_lib.SteamAPI_ISteamMatchmakingServers_RefreshQuery.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServers_RefreshQuery.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_IsRefreshing

steam_lib.SteamAPI_ISteamMatchmakingServers_IsRefreshing.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServers_IsRefreshing.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_GetServerCount

steam_lib.SteamAPI_ISteamMatchmakingServers_GetServerCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServers_GetServerCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_RefreshServer

steam_lib.SteamAPI_ISteamMatchmakingServers_RefreshServer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServers_RefreshServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_PingServer

steam_lib.SteamAPI_ISteamMatchmakingServers_PingServer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_PingServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_PlayerDetails

steam_lib.SteamAPI_ISteamMatchmakingServers_PlayerDetails.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_PlayerDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_ServerRules

steam_lib.SteamAPI_ISteamMatchmakingServers_ServerRules.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMatchmakingServers_ServerRules.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMatchmakingServers_CancelServerQuery

steam_lib.SteamAPI_ISteamMatchmakingServers_CancelServerQuery.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMatchmakingServers_CancelServerQuery.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_AddGameSearchParams

steam_lib.SteamAPI_ISteamGameSearch_AddGameSearchParams.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameSearch_AddGameSearchParams.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_SearchForGameWithLobby

steam_lib.SteamAPI_ISteamGameSearch_SearchForGameWithLobby.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameSearch_SearchForGameWithLobby.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_SearchForGameSolo

steam_lib.SteamAPI_ISteamGameSearch_SearchForGameSolo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameSearch_SearchForGameSolo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_AcceptGame

steam_lib.SteamAPI_ISteamGameSearch_AcceptGame.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameSearch_AcceptGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_DeclineGame

steam_lib.SteamAPI_ISteamGameSearch_DeclineGame.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameSearch_DeclineGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_RetrieveConnectionDetails

steam_lib.SteamAPI_ISteamGameSearch_RetrieveConnectionDetails.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameSearch_RetrieveConnectionDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_EndGameSearch

steam_lib.SteamAPI_ISteamGameSearch_EndGameSearch.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameSearch_EndGameSearch.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_SetGameHostParams

steam_lib.SteamAPI_ISteamGameSearch_SetGameHostParams.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameSearch_SetGameHostParams.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_SetConnectionDetails

steam_lib.SteamAPI_ISteamGameSearch_SetConnectionDetails.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameSearch_SetConnectionDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_RequestPlayersForGame

steam_lib.SteamAPI_ISteamGameSearch_RequestPlayersForGame.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameSearch_RequestPlayersForGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_HostConfirmGameStart

steam_lib.SteamAPI_ISteamGameSearch_HostConfirmGameStart.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameSearch_HostConfirmGameStart.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_CancelRequestPlayersForGame

steam_lib.SteamAPI_ISteamGameSearch_CancelRequestPlayersForGame.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameSearch_CancelRequestPlayersForGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_SubmitPlayerResult

steam_lib.SteamAPI_ISteamGameSearch_SubmitPlayerResult.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameSearch_SubmitPlayerResult.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameSearch_EndGame

steam_lib.SteamAPI_ISteamGameSearch_EndGame.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameSearch_EndGame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_GetNumActiveBeacons

steam_lib.SteamAPI_ISteamParties_GetNumActiveBeacons.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamParties_GetNumActiveBeacons.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_GetBeaconByIndex

steam_lib.SteamAPI_ISteamParties_GetBeaconByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_GetBeaconByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_GetBeaconDetails

steam_lib.SteamAPI_ISteamParties_GetBeaconDetails.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_GetBeaconDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_JoinParty

steam_lib.SteamAPI_ISteamParties_JoinParty.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_JoinParty.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_GetNumAvailableBeaconLocations

steam_lib.SteamAPI_ISteamParties_GetNumAvailableBeaconLocations.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamParties_GetNumAvailableBeaconLocations.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_GetAvailableBeaconLocations

steam_lib.SteamAPI_ISteamParties_GetAvailableBeaconLocations.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_GetAvailableBeaconLocations.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_CreateBeacon

steam_lib.SteamAPI_ISteamParties_CreateBeacon.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamParties_CreateBeacon.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_OnReservationCompleted

steam_lib.SteamAPI_ISteamParties_OnReservationCompleted.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_OnReservationCompleted.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_CancelReservation

steam_lib.SteamAPI_ISteamParties_CancelReservation.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_CancelReservation.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_ChangeNumOpenSlots

steam_lib.SteamAPI_ISteamParties_ChangeNumOpenSlots.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_ChangeNumOpenSlots.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_DestroyBeacon

steam_lib.SteamAPI_ISteamParties_DestroyBeacon.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_DestroyBeacon.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParties_GetBeaconLocationData

steam_lib.SteamAPI_ISteamParties_GetBeaconLocationData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParties_GetBeaconLocationData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileWrite

steam_lib.SteamAPI_ISteamRemoteStorage_FileWrite.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_FileWrite.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileRead

steam_lib.SteamAPI_ISteamRemoteStorage_FileRead.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_FileRead.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileWriteAsync

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteAsync.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteAsync.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileReadAsync

steam_lib.SteamAPI_ISteamRemoteStorage_FileReadAsync.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_FileReadAsync.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileReadAsyncComplete

steam_lib.SteamAPI_ISteamRemoteStorage_FileReadAsyncComplete.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_FileReadAsyncComplete.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileForget

steam_lib.SteamAPI_ISteamRemoteStorage_FileForget.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_FileForget.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileDelete

steam_lib.SteamAPI_ISteamRemoteStorage_FileDelete.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_FileDelete.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileShare

steam_lib.SteamAPI_ISteamRemoteStorage_FileShare.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_FileShare.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_SetSyncPlatforms

steam_lib.SteamAPI_ISteamRemoteStorage_SetSyncPlatforms.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_SetSyncPlatforms.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileWriteStreamOpen

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteStreamOpen.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteStreamOpen.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileWriteStreamWriteChunk

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteStreamWriteChunk.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteStreamWriteChunk.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileWriteStreamClose

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteStreamClose.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteStreamClose.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileWriteStreamCancel

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteStreamCancel.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_FileWriteStreamCancel.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FileExists

steam_lib.SteamAPI_ISteamRemoteStorage_FileExists.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_FileExists.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_FilePersisted

steam_lib.SteamAPI_ISteamRemoteStorage_FilePersisted.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_FilePersisted.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetFileSize

steam_lib.SteamAPI_ISteamRemoteStorage_GetFileSize.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetFileSize.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetFileTimestamp

steam_lib.SteamAPI_ISteamRemoteStorage_GetFileTimestamp.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetFileTimestamp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetSyncPlatforms

steam_lib.SteamAPI_ISteamRemoteStorage_GetSyncPlatforms.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetSyncPlatforms.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetFileCount

steam_lib.SteamAPI_ISteamRemoteStorage_GetFileCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetFileCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetFileNameAndSize

steam_lib.SteamAPI_ISteamRemoteStorage_GetFileNameAndSize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetFileNameAndSize.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetQuota

steam_lib.SteamAPI_ISteamRemoteStorage_GetQuota.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetQuota.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_IsCloudEnabledForAccount

steam_lib.SteamAPI_ISteamRemoteStorage_IsCloudEnabledForAccount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_IsCloudEnabledForAccount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_IsCloudEnabledForApp

steam_lib.SteamAPI_ISteamRemoteStorage_IsCloudEnabledForApp.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_IsCloudEnabledForApp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_SetCloudEnabledForApp

steam_lib.SteamAPI_ISteamRemoteStorage_SetCloudEnabledForApp.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_SetCloudEnabledForApp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UGCDownload

steam_lib.SteamAPI_ISteamRemoteStorage_UGCDownload.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_UGCDownload.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetUGCDownloadProgress

steam_lib.SteamAPI_ISteamRemoteStorage_GetUGCDownloadProgress.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetUGCDownloadProgress.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetUGCDetails

steam_lib.SteamAPI_ISteamRemoteStorage_GetUGCDetails.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetUGCDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UGCRead

steam_lib.SteamAPI_ISteamRemoteStorage_UGCRead.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_UGCRead.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetCachedUGCCount

steam_lib.SteamAPI_ISteamRemoteStorage_GetCachedUGCCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetCachedUGCCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetCachedUGCHandle

steam_lib.SteamAPI_ISteamRemoteStorage_GetCachedUGCHandle.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_GetCachedUGCHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_PublishWorkshopFile

steam_lib.SteamAPI_ISteamRemoteStorage_PublishWorkshopFile.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_PublishWorkshopFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_CreatePublishedFileUpdateRequest

steam_lib.SteamAPI_ISteamRemoteStorage_CreatePublishedFileUpdateRequest.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_CreatePublishedFileUpdateRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UpdatePublishedFileFile

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileFile.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UpdatePublishedFilePreviewFile

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFilePreviewFile.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFilePreviewFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTitle

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTitle.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTitle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UpdatePublishedFileDescription

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileDescription.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileDescription.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UpdatePublishedFileVisibility

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileVisibility.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileVisibility.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTags

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTags.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileTags.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_CommitPublishedFileUpdate

steam_lib.SteamAPI_ISteamRemoteStorage_CommitPublishedFileUpdate.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_CommitPublishedFileUpdate.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetPublishedFileDetails

steam_lib.SteamAPI_ISteamRemoteStorage_GetPublishedFileDetails.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_GetPublishedFileDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_DeletePublishedFile

steam_lib.SteamAPI_ISteamRemoteStorage_DeletePublishedFile.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_DeletePublishedFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_EnumerateUserPublishedFiles

steam_lib.SteamAPI_ISteamRemoteStorage_EnumerateUserPublishedFiles.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_EnumerateUserPublishedFiles.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_SubscribePublishedFile

steam_lib.SteamAPI_ISteamRemoteStorage_SubscribePublishedFile.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_SubscribePublishedFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_EnumerateUserSubscribedFiles

steam_lib.SteamAPI_ISteamRemoteStorage_EnumerateUserSubscribedFiles.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_EnumerateUserSubscribedFiles.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UnsubscribePublishedFile

steam_lib.SteamAPI_ISteamRemoteStorage_UnsubscribePublishedFile.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_UnsubscribePublishedFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_UpdatePublishedFileSetChangeDescription.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetPublishedItemVoteDetails

steam_lib.SteamAPI_ISteamRemoteStorage_GetPublishedItemVoteDetails.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_GetPublishedItemVoteDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UpdateUserPublishedItemVote

steam_lib.SteamAPI_ISteamRemoteStorage_UpdateUserPublishedItemVote.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_UpdateUserPublishedItemVote.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetUserPublishedItemVoteDetails

steam_lib.SteamAPI_ISteamRemoteStorage_GetUserPublishedItemVoteDetails.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_GetUserPublishedItemVoteDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles

steam_lib.SteamAPI_ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_EnumerateUserSharedWorkshopFiles.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_PublishVideo

steam_lib.SteamAPI_ISteamRemoteStorage_PublishVideo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_PublishVideo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_SetUserPublishedFileAction

steam_lib.SteamAPI_ISteamRemoteStorage_SetUserPublishedFileAction.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_SetUserPublishedFileAction.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_EnumeratePublishedFilesByUserAction

steam_lib.SteamAPI_ISteamRemoteStorage_EnumeratePublishedFilesByUserAction.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_EnumeratePublishedFilesByUserAction.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_EnumeratePublishedWorkshopFiles

steam_lib.SteamAPI_ISteamRemoteStorage_EnumeratePublishedWorkshopFiles.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_EnumeratePublishedWorkshopFiles.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_UGCDownloadToLocation

steam_lib.SteamAPI_ISteamRemoteStorage_UGCDownloadToLocation.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemoteStorage_UGCDownloadToLocation.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetLocalFileChangeCount

steam_lib.SteamAPI_ISteamRemoteStorage_GetLocalFileChangeCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetLocalFileChangeCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_GetLocalFileChange

steam_lib.SteamAPI_ISteamRemoteStorage_GetLocalFileChange.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_GetLocalFileChange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_BeginFileWriteBatch

steam_lib.SteamAPI_ISteamRemoteStorage_BeginFileWriteBatch.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_BeginFileWriteBatch.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemoteStorage_EndFileWriteBatch

steam_lib.SteamAPI_ISteamRemoteStorage_EndFileWriteBatch.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemoteStorage_EndFileWriteBatch.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetStatInt32

steam_lib.SteamAPI_ISteamUserStats_GetStatInt32.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetStatInt32.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetStatFloat

steam_lib.SteamAPI_ISteamUserStats_GetStatFloat.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetStatFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_SetStatInt32

steam_lib.SteamAPI_ISteamUserStats_SetStatInt32.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_SetStatInt32.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_SetStatFloat

steam_lib.SteamAPI_ISteamUserStats_SetStatFloat.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_SetStatFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_UpdateAvgRateStat

steam_lib.SteamAPI_ISteamUserStats_UpdateAvgRateStat.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_UpdateAvgRateStat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetAchievement

steam_lib.SteamAPI_ISteamUserStats_GetAchievement.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetAchievement.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_SetAchievement

steam_lib.SteamAPI_ISteamUserStats_SetAchievement.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_SetAchievement.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_ClearAchievement

steam_lib.SteamAPI_ISteamUserStats_ClearAchievement.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_ClearAchievement.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetAchievementAndUnlockTime

steam_lib.SteamAPI_ISteamUserStats_GetAchievementAndUnlockTime.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetAchievementAndUnlockTime.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_StoreStats

steam_lib.SteamAPI_ISteamUserStats_StoreStats.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_StoreStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetAchievementIcon

steam_lib.SteamAPI_ISteamUserStats_GetAchievementIcon.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetAchievementIcon.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetAchievementDisplayAttribute

steam_lib.SteamAPI_ISteamUserStats_GetAchievementDisplayAttribute.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetAchievementDisplayAttribute.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_IndicateAchievementProgress

steam_lib.SteamAPI_ISteamUserStats_IndicateAchievementProgress.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_IndicateAchievementProgress.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetNumAchievements

steam_lib.SteamAPI_ISteamUserStats_GetNumAchievements.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetNumAchievements.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetAchievementName

steam_lib.SteamAPI_ISteamUserStats_GetAchievementName.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_GetAchievementName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_RequestUserStats

steam_lib.SteamAPI_ISteamUserStats_RequestUserStats.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_RequestUserStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetUserStatInt32

steam_lib.SteamAPI_ISteamUserStats_GetUserStatInt32.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetUserStatInt32.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetUserStatFloat

steam_lib.SteamAPI_ISteamUserStats_GetUserStatFloat.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetUserStatFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetUserAchievement

steam_lib.SteamAPI_ISteamUserStats_GetUserAchievement.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetUserAchievement.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetUserAchievementAndUnlockTime

steam_lib.SteamAPI_ISteamUserStats_GetUserAchievementAndUnlockTime.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetUserAchievementAndUnlockTime.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_ResetAllStats

steam_lib.SteamAPI_ISteamUserStats_ResetAllStats.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_ResetAllStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_FindOrCreateLeaderboard

steam_lib.SteamAPI_ISteamUserStats_FindOrCreateLeaderboard.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_FindOrCreateLeaderboard.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_FindLeaderboard

steam_lib.SteamAPI_ISteamUserStats_FindLeaderboard.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_FindLeaderboard.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetLeaderboardName

steam_lib.SteamAPI_ISteamUserStats_GetLeaderboardName.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_GetLeaderboardName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetLeaderboardEntryCount

steam_lib.SteamAPI_ISteamUserStats_GetLeaderboardEntryCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_GetLeaderboardEntryCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetLeaderboardSortMethod

steam_lib.SteamAPI_ISteamUserStats_GetLeaderboardSortMethod.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_GetLeaderboardSortMethod.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetLeaderboardDisplayType

steam_lib.SteamAPI_ISteamUserStats_GetLeaderboardDisplayType.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_GetLeaderboardDisplayType.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_DownloadLeaderboardEntries

steam_lib.SteamAPI_ISteamUserStats_DownloadLeaderboardEntries.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_DownloadLeaderboardEntries.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_DownloadLeaderboardEntriesForUsers

steam_lib.SteamAPI_ISteamUserStats_DownloadLeaderboardEntriesForUsers.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_DownloadLeaderboardEntriesForUsers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetDownloadedLeaderboardEntry

steam_lib.SteamAPI_ISteamUserStats_GetDownloadedLeaderboardEntry.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_GetDownloadedLeaderboardEntry.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_UploadLeaderboardScore

steam_lib.SteamAPI_ISteamUserStats_UploadLeaderboardScore.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_UploadLeaderboardScore.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_AttachLeaderboardUGC

steam_lib.SteamAPI_ISteamUserStats_AttachLeaderboardUGC.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_AttachLeaderboardUGC.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetNumberOfCurrentPlayers

steam_lib.SteamAPI_ISteamUserStats_GetNumberOfCurrentPlayers.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetNumberOfCurrentPlayers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_RequestGlobalAchievementPercentages

steam_lib.SteamAPI_ISteamUserStats_RequestGlobalAchievementPercentages.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_RequestGlobalAchievementPercentages.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetMostAchievedAchievementInfo

steam_lib.SteamAPI_ISteamUserStats_GetMostAchievedAchievementInfo.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetMostAchievedAchievementInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetNextMostAchievedAchievementInfo

steam_lib.SteamAPI_ISteamUserStats_GetNextMostAchievedAchievementInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetNextMostAchievedAchievementInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetAchievementAchievedPercent

steam_lib.SteamAPI_ISteamUserStats_GetAchievementAchievedPercent.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetAchievementAchievedPercent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_RequestGlobalStats

steam_lib.SteamAPI_ISteamUserStats_RequestGlobalStats.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_RequestGlobalStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetGlobalStatInt64

steam_lib.SteamAPI_ISteamUserStats_GetGlobalStatInt64.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetGlobalStatInt64.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetGlobalStatDouble

steam_lib.SteamAPI_ISteamUserStats_GetGlobalStatDouble.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetGlobalStatDouble.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetGlobalStatHistoryInt64

steam_lib.SteamAPI_ISteamUserStats_GetGlobalStatHistoryInt64.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_GetGlobalStatHistoryInt64.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetGlobalStatHistoryDouble

steam_lib.SteamAPI_ISteamUserStats_GetGlobalStatHistoryDouble.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUserStats_GetGlobalStatHistoryDouble.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetAchievementProgressLimitsInt32

steam_lib.SteamAPI_ISteamUserStats_GetAchievementProgressLimitsInt32.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetAchievementProgressLimitsInt32.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUserStats_GetAchievementProgressLimitsFloat

steam_lib.SteamAPI_ISteamUserStats_GetAchievementProgressLimitsFloat.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUserStats_GetAchievementProgressLimitsFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsSubscribed

steam_lib.SteamAPI_ISteamApps_BIsSubscribed.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_BIsSubscribed.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsLowViolence

steam_lib.SteamAPI_ISteamApps_BIsLowViolence.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_BIsLowViolence.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsCybercafe

steam_lib.SteamAPI_ISteamApps_BIsCybercafe.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_BIsCybercafe.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsVACBanned

steam_lib.SteamAPI_ISteamApps_BIsVACBanned.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_BIsVACBanned.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetCurrentGameLanguage

steam_lib.SteamAPI_ISteamApps_GetCurrentGameLanguage.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetCurrentGameLanguage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetAvailableGameLanguages

steam_lib.SteamAPI_ISteamApps_GetAvailableGameLanguages.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetAvailableGameLanguages.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsSubscribedApp

steam_lib.SteamAPI_ISteamApps_BIsSubscribedApp.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_BIsSubscribedApp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsDlcInstalled

steam_lib.SteamAPI_ISteamApps_BIsDlcInstalled.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_BIsDlcInstalled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetEarliestPurchaseUnixTime

steam_lib.SteamAPI_ISteamApps_GetEarliestPurchaseUnixTime.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_GetEarliestPurchaseUnixTime.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsSubscribedFromFreeWeekend

steam_lib.SteamAPI_ISteamApps_BIsSubscribedFromFreeWeekend.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_BIsSubscribedFromFreeWeekend.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetDLCCount

steam_lib.SteamAPI_ISteamApps_GetDLCCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetDLCCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BGetDLCDataByIndex

steam_lib.SteamAPI_ISteamApps_BGetDLCDataByIndex.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_BGetDLCDataByIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_InstallDLC

steam_lib.SteamAPI_ISteamApps_InstallDLC.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_InstallDLC.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_UninstallDLC

steam_lib.SteamAPI_ISteamApps_UninstallDLC.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_UninstallDLC.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_RequestAppProofOfPurchaseKey

steam_lib.SteamAPI_ISteamApps_RequestAppProofOfPurchaseKey.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_RequestAppProofOfPurchaseKey.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetCurrentBetaName

steam_lib.SteamAPI_ISteamApps_GetCurrentBetaName.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_GetCurrentBetaName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_MarkContentCorrupt

steam_lib.SteamAPI_ISteamApps_MarkContentCorrupt.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_MarkContentCorrupt.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetInstalledDepots

steam_lib.SteamAPI_ISteamApps_GetInstalledDepots.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_GetInstalledDepots.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetAppInstallDir

steam_lib.SteamAPI_ISteamApps_GetAppInstallDir.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_GetAppInstallDir.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsAppInstalled

steam_lib.SteamAPI_ISteamApps_BIsAppInstalled.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_BIsAppInstalled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetAppOwner

steam_lib.SteamAPI_ISteamApps_GetAppOwner.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetAppOwner.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetLaunchQueryParam

steam_lib.SteamAPI_ISteamApps_GetLaunchQueryParam.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetLaunchQueryParam.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetDlcDownloadProgress

steam_lib.SteamAPI_ISteamApps_GetDlcDownloadProgress.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetDlcDownloadProgress.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetAppBuildId

steam_lib.SteamAPI_ISteamApps_GetAppBuildId.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetAppBuildId.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_RequestAllProofOfPurchaseKeys

steam_lib.SteamAPI_ISteamApps_RequestAllProofOfPurchaseKeys.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_RequestAllProofOfPurchaseKeys.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetFileDetails

steam_lib.SteamAPI_ISteamApps_GetFileDetails.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetFileDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetLaunchCommandLine

steam_lib.SteamAPI_ISteamApps_GetLaunchCommandLine.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_GetLaunchCommandLine.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsSubscribedFromFamilySharing

steam_lib.SteamAPI_ISteamApps_BIsSubscribedFromFamilySharing.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_BIsSubscribedFromFamilySharing.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_BIsTimedTrial

steam_lib.SteamAPI_ISteamApps_BIsTimedTrial.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_BIsTimedTrial.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_SetDlcContext

steam_lib.SteamAPI_ISteamApps_SetDlcContext.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_SetDlcContext.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetNumBetas

steam_lib.SteamAPI_ISteamApps_GetNumBetas.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_GetNumBetas.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_GetBetaInfo

steam_lib.SteamAPI_ISteamApps_GetBetaInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamApps_GetBetaInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamApps_SetActiveBeta

steam_lib.SteamAPI_ISteamApps_SetActiveBeta.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamApps_SetActiveBeta.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_SendP2PPacket

steam_lib.SteamAPI_ISteamNetworking_SendP2PPacket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_SendP2PPacket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_IsP2PPacketAvailable

steam_lib.SteamAPI_ISteamNetworking_IsP2PPacketAvailable.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_IsP2PPacketAvailable.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_ReadP2PPacket

steam_lib.SteamAPI_ISteamNetworking_ReadP2PPacket.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_ReadP2PPacket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_AcceptP2PSessionWithUser

steam_lib.SteamAPI_ISteamNetworking_AcceptP2PSessionWithUser.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_AcceptP2PSessionWithUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_CloseP2PSessionWithUser

steam_lib.SteamAPI_ISteamNetworking_CloseP2PSessionWithUser.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_CloseP2PSessionWithUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_CloseP2PChannelWithUser

steam_lib.SteamAPI_ISteamNetworking_CloseP2PChannelWithUser.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_CloseP2PChannelWithUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_GetP2PSessionState

steam_lib.SteamAPI_ISteamNetworking_GetP2PSessionState.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworking_GetP2PSessionState.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_AllowP2PPacketRelay

steam_lib.SteamAPI_ISteamNetworking_AllowP2PPacketRelay.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_AllowP2PPacketRelay.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_CreateListenSocket

steam_lib.SteamAPI_ISteamNetworking_CreateListenSocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_CreateListenSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_CreateP2PConnectionSocket

steam_lib.SteamAPI_ISteamNetworking_CreateP2PConnectionSocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_CreateP2PConnectionSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_CreateConnectionSocket

steam_lib.SteamAPI_ISteamNetworking_CreateConnectionSocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_CreateConnectionSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_DestroySocket

steam_lib.SteamAPI_ISteamNetworking_DestroySocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_DestroySocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_DestroyListenSocket

steam_lib.SteamAPI_ISteamNetworking_DestroyListenSocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_DestroyListenSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_SendDataOnSocket

steam_lib.SteamAPI_ISteamNetworking_SendDataOnSocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_SendDataOnSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_IsDataAvailableOnSocket

steam_lib.SteamAPI_ISteamNetworking_IsDataAvailableOnSocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworking_IsDataAvailableOnSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_RetrieveDataFromSocket

steam_lib.SteamAPI_ISteamNetworking_RetrieveDataFromSocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworking_RetrieveDataFromSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_IsDataAvailable

steam_lib.SteamAPI_ISteamNetworking_IsDataAvailable.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworking_IsDataAvailable.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_RetrieveData

steam_lib.SteamAPI_ISteamNetworking_RetrieveData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworking_RetrieveData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_GetSocketInfo

steam_lib.SteamAPI_ISteamNetworking_GetSocketInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworking_GetSocketInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_GetListenSocketInfo

steam_lib.SteamAPI_ISteamNetworking_GetListenSocketInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworking_GetListenSocketInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_GetSocketConnectionType

steam_lib.SteamAPI_ISteamNetworking_GetSocketConnectionType.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_GetSocketConnectionType.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworking_GetMaxPacketSize

steam_lib.SteamAPI_ISteamNetworking_GetMaxPacketSize.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworking_GetMaxPacketSize.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_WriteScreenshot

steam_lib.SteamAPI_ISteamScreenshots_WriteScreenshot.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamScreenshots_WriteScreenshot.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_AddScreenshotToLibrary

steam_lib.SteamAPI_ISteamScreenshots_AddScreenshotToLibrary.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamScreenshots_AddScreenshotToLibrary.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_TriggerScreenshot

steam_lib.SteamAPI_ISteamScreenshots_TriggerScreenshot.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamScreenshots_TriggerScreenshot.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_HookScreenshots

steam_lib.SteamAPI_ISteamScreenshots_HookScreenshots.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamScreenshots_HookScreenshots.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_SetLocation

steam_lib.SteamAPI_ISteamScreenshots_SetLocation.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamScreenshots_SetLocation.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_TagUser

steam_lib.SteamAPI_ISteamScreenshots_TagUser.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamScreenshots_TagUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_TagPublishedFile

steam_lib.SteamAPI_ISteamScreenshots_TagPublishedFile.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamScreenshots_TagPublishedFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_IsScreenshotsHooked

steam_lib.SteamAPI_ISteamScreenshots_IsScreenshotsHooked.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamScreenshots_IsScreenshotsHooked.restype = ctypes.c_int


# Binding for SteamAPI_ISteamScreenshots_AddVRScreenshotToLibrary

steam_lib.SteamAPI_ISteamScreenshots_AddVRScreenshotToLibrary.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamScreenshots_AddVRScreenshotToLibrary.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_BIsEnabled

steam_lib.SteamAPI_ISteamMusic_BIsEnabled.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusic_BIsEnabled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_BIsPlaying

steam_lib.SteamAPI_ISteamMusic_BIsPlaying.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusic_BIsPlaying.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_GetPlaybackStatus

steam_lib.SteamAPI_ISteamMusic_GetPlaybackStatus.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusic_GetPlaybackStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_Play

steam_lib.SteamAPI_ISteamMusic_Play.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusic_Play.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_Pause

steam_lib.SteamAPI_ISteamMusic_Pause.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusic_Pause.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_PlayPrevious

steam_lib.SteamAPI_ISteamMusic_PlayPrevious.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusic_PlayPrevious.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_PlayNext

steam_lib.SteamAPI_ISteamMusic_PlayNext.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusic_PlayNext.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_SetVolume

steam_lib.SteamAPI_ISteamMusic_SetVolume.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusic_SetVolume.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusic_GetVolume

steam_lib.SteamAPI_ISteamMusic_GetVolume.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusic_GetVolume.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_RegisterSteamMusicRemote

steam_lib.SteamAPI_ISteamMusicRemote_RegisterSteamMusicRemote.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_RegisterSteamMusicRemote.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_DeregisterSteamMusicRemote

steam_lib.SteamAPI_ISteamMusicRemote_DeregisterSteamMusicRemote.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_DeregisterSteamMusicRemote.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_BIsCurrentMusicRemote

steam_lib.SteamAPI_ISteamMusicRemote_BIsCurrentMusicRemote.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_BIsCurrentMusicRemote.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_BActivationSuccess

steam_lib.SteamAPI_ISteamMusicRemote_BActivationSuccess.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_BActivationSuccess.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_SetDisplayName

steam_lib.SteamAPI_ISteamMusicRemote_SetDisplayName.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_SetDisplayName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_SetPNGIcon_64x64

steam_lib.SteamAPI_ISteamMusicRemote_SetPNGIcon_64x64.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_SetPNGIcon_64x64.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_EnablePlayPrevious

steam_lib.SteamAPI_ISteamMusicRemote_EnablePlayPrevious.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_EnablePlayPrevious.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_EnablePlayNext

steam_lib.SteamAPI_ISteamMusicRemote_EnablePlayNext.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_EnablePlayNext.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_EnableShuffled

steam_lib.SteamAPI_ISteamMusicRemote_EnableShuffled.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_EnableShuffled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_EnableLooped

steam_lib.SteamAPI_ISteamMusicRemote_EnableLooped.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_EnableLooped.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_EnableQueue

steam_lib.SteamAPI_ISteamMusicRemote_EnableQueue.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_EnableQueue.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_EnablePlaylists

steam_lib.SteamAPI_ISteamMusicRemote_EnablePlaylists.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_EnablePlaylists.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_UpdatePlaybackStatus

steam_lib.SteamAPI_ISteamMusicRemote_UpdatePlaybackStatus.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_UpdatePlaybackStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_UpdateShuffled

steam_lib.SteamAPI_ISteamMusicRemote_UpdateShuffled.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_UpdateShuffled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_UpdateLooped

steam_lib.SteamAPI_ISteamMusicRemote_UpdateLooped.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_UpdateLooped.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_UpdateVolume

steam_lib.SteamAPI_ISteamMusicRemote_UpdateVolume.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_UpdateVolume.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_CurrentEntryWillChange

steam_lib.SteamAPI_ISteamMusicRemote_CurrentEntryWillChange.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_CurrentEntryWillChange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_CurrentEntryIsAvailable

steam_lib.SteamAPI_ISteamMusicRemote_CurrentEntryIsAvailable.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_CurrentEntryIsAvailable.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_UpdateCurrentEntryText

steam_lib.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryText.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryText.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds

steam_lib.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryElapsedSeconds.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_UpdateCurrentEntryCoverArt

steam_lib.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryCoverArt.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_UpdateCurrentEntryCoverArt.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_CurrentEntryDidChange

steam_lib.SteamAPI_ISteamMusicRemote_CurrentEntryDidChange.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_CurrentEntryDidChange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_QueueWillChange

steam_lib.SteamAPI_ISteamMusicRemote_QueueWillChange.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_QueueWillChange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_ResetQueueEntries

steam_lib.SteamAPI_ISteamMusicRemote_ResetQueueEntries.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_ResetQueueEntries.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_SetQueueEntry

steam_lib.SteamAPI_ISteamMusicRemote_SetQueueEntry.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_SetQueueEntry.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_SetCurrentQueueEntry

steam_lib.SteamAPI_ISteamMusicRemote_SetCurrentQueueEntry.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_SetCurrentQueueEntry.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_QueueDidChange

steam_lib.SteamAPI_ISteamMusicRemote_QueueDidChange.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_QueueDidChange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_PlaylistWillChange

steam_lib.SteamAPI_ISteamMusicRemote_PlaylistWillChange.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_PlaylistWillChange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_ResetPlaylistEntries

steam_lib.SteamAPI_ISteamMusicRemote_ResetPlaylistEntries.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_ResetPlaylistEntries.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_SetPlaylistEntry

steam_lib.SteamAPI_ISteamMusicRemote_SetPlaylistEntry.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_SetPlaylistEntry.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_SetCurrentPlaylistEntry

steam_lib.SteamAPI_ISteamMusicRemote_SetCurrentPlaylistEntry.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamMusicRemote_SetCurrentPlaylistEntry.restype = ctypes.c_int


# Binding for SteamAPI_ISteamMusicRemote_PlaylistDidChange

steam_lib.SteamAPI_ISteamMusicRemote_PlaylistDidChange.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamMusicRemote_PlaylistDidChange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_CreateHTTPRequest

steam_lib.SteamAPI_ISteamHTTP_CreateHTTPRequest.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_CreateHTTPRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestContextValue

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestContextValue.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestContextValue.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestNetworkActivityTimeout

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestNetworkActivityTimeout.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestNetworkActivityTimeout.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestHeaderValue

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestHeaderValue.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestHeaderValue.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestGetOrPostParameter

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestGetOrPostParameter.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestGetOrPostParameter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SendHTTPRequest

steam_lib.SteamAPI_ISteamHTTP_SendHTTPRequest.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_SendHTTPRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SendHTTPRequestAndStreamResponse

steam_lib.SteamAPI_ISteamHTTP_SendHTTPRequestAndStreamResponse.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_SendHTTPRequestAndStreamResponse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_DeferHTTPRequest

steam_lib.SteamAPI_ISteamHTTP_DeferHTTPRequest.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_DeferHTTPRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_PrioritizeHTTPRequest

steam_lib.SteamAPI_ISteamHTTP_PrioritizeHTTPRequest.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_PrioritizeHTTPRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_GetHTTPResponseHeaderSize

steam_lib.SteamAPI_ISteamHTTP_GetHTTPResponseHeaderSize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_GetHTTPResponseHeaderSize.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_GetHTTPResponseHeaderValue

steam_lib.SteamAPI_ISteamHTTP_GetHTTPResponseHeaderValue.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_GetHTTPResponseHeaderValue.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_GetHTTPResponseBodySize

steam_lib.SteamAPI_ISteamHTTP_GetHTTPResponseBodySize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_GetHTTPResponseBodySize.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_GetHTTPResponseBodyData

steam_lib.SteamAPI_ISteamHTTP_GetHTTPResponseBodyData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_GetHTTPResponseBodyData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_GetHTTPStreamingResponseBodyData

steam_lib.SteamAPI_ISteamHTTP_GetHTTPStreamingResponseBodyData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_GetHTTPStreamingResponseBodyData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_ReleaseHTTPRequest

steam_lib.SteamAPI_ISteamHTTP_ReleaseHTTPRequest.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_ReleaseHTTPRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_GetHTTPDownloadProgressPct

steam_lib.SteamAPI_ISteamHTTP_GetHTTPDownloadProgressPct.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_GetHTTPDownloadProgressPct.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestRawPostBody

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestRawPostBody.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestRawPostBody.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_CreateCookieContainer

steam_lib.SteamAPI_ISteamHTTP_CreateCookieContainer.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_CreateCookieContainer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_ReleaseCookieContainer

steam_lib.SteamAPI_ISteamHTTP_ReleaseCookieContainer.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_ReleaseCookieContainer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetCookie

steam_lib.SteamAPI_ISteamHTTP_SetCookie.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_SetCookie.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestCookieContainer

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestCookieContainer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestCookieContainer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestUserAgentInfo

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestUserAgentInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestUserAgentInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestRequiresVerifiedCertificate.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTTP_SetHTTPRequestAbsoluteTimeoutMS.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTTP_GetHTTPRequestWasTimedOut

steam_lib.SteamAPI_ISteamHTTP_GetHTTPRequestWasTimedOut.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTTP_GetHTTPRequestWasTimedOut.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_Init

steam_lib.SteamAPI_ISteamInput_Init.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_Init.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_Shutdown

steam_lib.SteamAPI_ISteamInput_Shutdown.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_Shutdown.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_SetInputActionManifestFilePath

steam_lib.SteamAPI_ISteamInput_SetInputActionManifestFilePath.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_SetInputActionManifestFilePath.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_RunFrame

steam_lib.SteamAPI_ISteamInput_RunFrame.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_RunFrame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_BWaitForData

steam_lib.SteamAPI_ISteamInput_BWaitForData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_BWaitForData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_BNewDataAvailable

steam_lib.SteamAPI_ISteamInput_BNewDataAvailable.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_BNewDataAvailable.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetConnectedControllers

steam_lib.SteamAPI_ISteamInput_GetConnectedControllers.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetConnectedControllers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_EnableDeviceCallbacks

steam_lib.SteamAPI_ISteamInput_EnableDeviceCallbacks.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_EnableDeviceCallbacks.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_EnableActionEventCallbacks

steam_lib.SteamAPI_ISteamInput_EnableActionEventCallbacks.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_EnableActionEventCallbacks.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetActionSetHandle

steam_lib.SteamAPI_ISteamInput_GetActionSetHandle.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetActionSetHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_ActivateActionSet

steam_lib.SteamAPI_ISteamInput_ActivateActionSet.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_ActivateActionSet.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetCurrentActionSet

steam_lib.SteamAPI_ISteamInput_GetCurrentActionSet.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetCurrentActionSet.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_ActivateActionSetLayer

steam_lib.SteamAPI_ISteamInput_ActivateActionSetLayer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_ActivateActionSetLayer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_DeactivateActionSetLayer

steam_lib.SteamAPI_ISteamInput_DeactivateActionSetLayer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_DeactivateActionSetLayer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_DeactivateAllActionSetLayers

steam_lib.SteamAPI_ISteamInput_DeactivateAllActionSetLayers.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_DeactivateAllActionSetLayers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetActiveActionSetLayers

steam_lib.SteamAPI_ISteamInput_GetActiveActionSetLayers.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetActiveActionSetLayers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetDigitalActionHandle

steam_lib.SteamAPI_ISteamInput_GetDigitalActionHandle.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetDigitalActionHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetDigitalActionData

steam_lib.SteamAPI_ISteamInput_GetDigitalActionData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetDigitalActionData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetDigitalActionOrigins

steam_lib.SteamAPI_ISteamInput_GetDigitalActionOrigins.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetDigitalActionOrigins.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetStringForDigitalActionName

steam_lib.SteamAPI_ISteamInput_GetStringForDigitalActionName.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetStringForDigitalActionName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetAnalogActionHandle

steam_lib.SteamAPI_ISteamInput_GetAnalogActionHandle.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetAnalogActionHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetAnalogActionData

steam_lib.SteamAPI_ISteamInput_GetAnalogActionData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetAnalogActionData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetAnalogActionOrigins

steam_lib.SteamAPI_ISteamInput_GetAnalogActionOrigins.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetAnalogActionOrigins.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetGlyphPNGForActionOrigin

steam_lib.SteamAPI_ISteamInput_GetGlyphPNGForActionOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetGlyphPNGForActionOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetGlyphSVGForActionOrigin

steam_lib.SteamAPI_ISteamInput_GetGlyphSVGForActionOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetGlyphSVGForActionOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetGlyphForActionOrigin_Legacy

steam_lib.SteamAPI_ISteamInput_GetGlyphForActionOrigin_Legacy.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetGlyphForActionOrigin_Legacy.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetStringForActionOrigin

steam_lib.SteamAPI_ISteamInput_GetStringForActionOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetStringForActionOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetStringForAnalogActionName

steam_lib.SteamAPI_ISteamInput_GetStringForAnalogActionName.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetStringForAnalogActionName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_StopAnalogActionMomentum

steam_lib.SteamAPI_ISteamInput_StopAnalogActionMomentum.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_StopAnalogActionMomentum.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetMotionData

steam_lib.SteamAPI_ISteamInput_GetMotionData.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetMotionData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_TriggerVibration

steam_lib.SteamAPI_ISteamInput_TriggerVibration.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_TriggerVibration.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_TriggerVibrationExtended

steam_lib.SteamAPI_ISteamInput_TriggerVibrationExtended.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_TriggerVibrationExtended.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_TriggerSimpleHapticEvent

steam_lib.SteamAPI_ISteamInput_TriggerSimpleHapticEvent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_TriggerSimpleHapticEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_SetLEDColor

steam_lib.SteamAPI_ISteamInput_SetLEDColor.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_SetLEDColor.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_Legacy_TriggerHapticPulse

steam_lib.SteamAPI_ISteamInput_Legacy_TriggerHapticPulse.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_Legacy_TriggerHapticPulse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_Legacy_TriggerRepeatedHapticPulse

steam_lib.SteamAPI_ISteamInput_Legacy_TriggerRepeatedHapticPulse.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_Legacy_TriggerRepeatedHapticPulse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_ShowBindingPanel

steam_lib.SteamAPI_ISteamInput_ShowBindingPanel.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_ShowBindingPanel.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetInputTypeForHandle

steam_lib.SteamAPI_ISteamInput_GetInputTypeForHandle.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetInputTypeForHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetControllerForGamepadIndex

steam_lib.SteamAPI_ISteamInput_GetControllerForGamepadIndex.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetControllerForGamepadIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetGamepadIndexForController

steam_lib.SteamAPI_ISteamInput_GetGamepadIndexForController.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetGamepadIndexForController.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetStringForXboxOrigin

steam_lib.SteamAPI_ISteamInput_GetStringForXboxOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetStringForXboxOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetGlyphForXboxOrigin

steam_lib.SteamAPI_ISteamInput_GetGlyphForXboxOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetGlyphForXboxOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetActionOriginFromXboxOrigin

steam_lib.SteamAPI_ISteamInput_GetActionOriginFromXboxOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetActionOriginFromXboxOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_TranslateActionOrigin

steam_lib.SteamAPI_ISteamInput_TranslateActionOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_TranslateActionOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetDeviceBindingRevision

steam_lib.SteamAPI_ISteamInput_GetDeviceBindingRevision.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetDeviceBindingRevision.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetRemotePlaySessionID

steam_lib.SteamAPI_ISteamInput_GetRemotePlaySessionID.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInput_GetRemotePlaySessionID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_GetSessionInputConfigurationSettings

steam_lib.SteamAPI_ISteamInput_GetSessionInputConfigurationSettings.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_GetSessionInputConfigurationSettings.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInput_SetDualSenseTriggerEffect

steam_lib.SteamAPI_ISteamInput_SetDualSenseTriggerEffect.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInput_SetDualSenseTriggerEffect.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_Init

steam_lib.SteamAPI_ISteamController_Init.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_Init.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_Shutdown

steam_lib.SteamAPI_ISteamController_Shutdown.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_Shutdown.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_RunFrame

steam_lib.SteamAPI_ISteamController_RunFrame.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_RunFrame.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetConnectedControllers

steam_lib.SteamAPI_ISteamController_GetConnectedControllers.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_GetConnectedControllers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetActionSetHandle

steam_lib.SteamAPI_ISteamController_GetActionSetHandle.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_GetActionSetHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_ActivateActionSet

steam_lib.SteamAPI_ISteamController_ActivateActionSet.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_ActivateActionSet.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetCurrentActionSet

steam_lib.SteamAPI_ISteamController_GetCurrentActionSet.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetCurrentActionSet.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_ActivateActionSetLayer

steam_lib.SteamAPI_ISteamController_ActivateActionSetLayer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_ActivateActionSetLayer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_DeactivateActionSetLayer

steam_lib.SteamAPI_ISteamController_DeactivateActionSetLayer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_DeactivateActionSetLayer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_DeactivateAllActionSetLayers

steam_lib.SteamAPI_ISteamController_DeactivateAllActionSetLayers.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_DeactivateAllActionSetLayers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetActiveActionSetLayers

steam_lib.SteamAPI_ISteamController_GetActiveActionSetLayers.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_GetActiveActionSetLayers.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetDigitalActionHandle

steam_lib.SteamAPI_ISteamController_GetDigitalActionHandle.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_GetDigitalActionHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetDigitalActionData

steam_lib.SteamAPI_ISteamController_GetDigitalActionData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetDigitalActionData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetDigitalActionOrigins

steam_lib.SteamAPI_ISteamController_GetDigitalActionOrigins.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_GetDigitalActionOrigins.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetAnalogActionHandle

steam_lib.SteamAPI_ISteamController_GetAnalogActionHandle.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_GetAnalogActionHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetAnalogActionData

steam_lib.SteamAPI_ISteamController_GetAnalogActionData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetAnalogActionData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetAnalogActionOrigins

steam_lib.SteamAPI_ISteamController_GetAnalogActionOrigins.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_GetAnalogActionOrigins.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetGlyphForActionOrigin

steam_lib.SteamAPI_ISteamController_GetGlyphForActionOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetGlyphForActionOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetStringForActionOrigin

steam_lib.SteamAPI_ISteamController_GetStringForActionOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetStringForActionOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_StopAnalogActionMomentum

steam_lib.SteamAPI_ISteamController_StopAnalogActionMomentum.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_StopAnalogActionMomentum.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetMotionData

steam_lib.SteamAPI_ISteamController_GetMotionData.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetMotionData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_TriggerHapticPulse

steam_lib.SteamAPI_ISteamController_TriggerHapticPulse.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_TriggerHapticPulse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_TriggerRepeatedHapticPulse

steam_lib.SteamAPI_ISteamController_TriggerRepeatedHapticPulse.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_TriggerRepeatedHapticPulse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_TriggerVibration

steam_lib.SteamAPI_ISteamController_TriggerVibration.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_TriggerVibration.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_SetLEDColor

steam_lib.SteamAPI_ISteamController_SetLEDColor.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_SetLEDColor.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_ShowBindingPanel

steam_lib.SteamAPI_ISteamController_ShowBindingPanel.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_ShowBindingPanel.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetInputTypeForHandle

steam_lib.SteamAPI_ISteamController_GetInputTypeForHandle.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetInputTypeForHandle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetControllerForGamepadIndex

steam_lib.SteamAPI_ISteamController_GetControllerForGamepadIndex.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetControllerForGamepadIndex.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetGamepadIndexForController

steam_lib.SteamAPI_ISteamController_GetGamepadIndexForController.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetGamepadIndexForController.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetStringForXboxOrigin

steam_lib.SteamAPI_ISteamController_GetStringForXboxOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetStringForXboxOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetGlyphForXboxOrigin

steam_lib.SteamAPI_ISteamController_GetGlyphForXboxOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetGlyphForXboxOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetActionOriginFromXboxOrigin

steam_lib.SteamAPI_ISteamController_GetActionOriginFromXboxOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_GetActionOriginFromXboxOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_TranslateActionOrigin

steam_lib.SteamAPI_ISteamController_TranslateActionOrigin.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamController_TranslateActionOrigin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamController_GetControllerBindingRevision

steam_lib.SteamAPI_ISteamController_GetControllerBindingRevision.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamController_GetControllerBindingRevision.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_CreateQueryUserUGCRequest

steam_lib.SteamAPI_ISteamUGC_CreateQueryUserUGCRequest.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_CreateQueryUserUGCRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_CreateQueryAllUGCRequestPage

steam_lib.SteamAPI_ISteamUGC_CreateQueryAllUGCRequestPage.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_CreateQueryAllUGCRequestPage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_CreateQueryAllUGCRequestCursor

steam_lib.SteamAPI_ISteamUGC_CreateQueryAllUGCRequestCursor.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_CreateQueryAllUGCRequestCursor.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_CreateQueryUGCDetailsRequest

steam_lib.SteamAPI_ISteamUGC_CreateQueryUGCDetailsRequest.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_CreateQueryUGCDetailsRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SendQueryUGCRequest

steam_lib.SteamAPI_ISteamUGC_SendQueryUGCRequest.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SendQueryUGCRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCResult

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCResult.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCResult.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCNumTags

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCNumTags.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCNumTags.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCTag

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCTag.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCTagDisplayName

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCTagDisplayName.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCTagDisplayName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCPreviewURL

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCPreviewURL.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCPreviewURL.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCMetadata

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCMetadata.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCMetadata.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCChildren

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCChildren.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCChildren.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCStatistic

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCStatistic.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCStatistic.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCNumAdditionalPreviews

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCNumAdditionalPreviews.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCNumAdditionalPreviews.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCAdditionalPreview

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCAdditionalPreview.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCAdditionalPreview.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCNumKeyValueTags

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCNumKeyValueTags.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCNumKeyValueTags.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCKeyValueTag

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCKeyValueTag.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCKeyValueTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryFirstUGCKeyValueTag

steam_lib.SteamAPI_ISteamUGC_GetQueryFirstUGCKeyValueTag.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryFirstUGCKeyValueTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetNumSupportedGameVersions

steam_lib.SteamAPI_ISteamUGC_GetNumSupportedGameVersions.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetNumSupportedGameVersions.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetSupportedGameVersionData

steam_lib.SteamAPI_ISteamUGC_GetSupportedGameVersionData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetSupportedGameVersionData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetQueryUGCContentDescriptors

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCContentDescriptors.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetQueryUGCContentDescriptors.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_ReleaseQueryUGCRequest

steam_lib.SteamAPI_ISteamUGC_ReleaseQueryUGCRequest.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_ReleaseQueryUGCRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddRequiredTag

steam_lib.SteamAPI_ISteamUGC_AddRequiredTag.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_AddRequiredTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddRequiredTagGroup

steam_lib.SteamAPI_ISteamUGC_AddRequiredTagGroup.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_AddRequiredTagGroup.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddExcludedTag

steam_lib.SteamAPI_ISteamUGC_AddExcludedTag.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_AddExcludedTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetReturnOnlyIDs

steam_lib.SteamAPI_ISteamUGC_SetReturnOnlyIDs.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetReturnOnlyIDs.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetReturnKeyValueTags

steam_lib.SteamAPI_ISteamUGC_SetReturnKeyValueTags.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetReturnKeyValueTags.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetReturnLongDescription

steam_lib.SteamAPI_ISteamUGC_SetReturnLongDescription.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetReturnLongDescription.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetReturnMetadata

steam_lib.SteamAPI_ISteamUGC_SetReturnMetadata.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetReturnMetadata.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetReturnChildren

steam_lib.SteamAPI_ISteamUGC_SetReturnChildren.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetReturnChildren.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetReturnAdditionalPreviews

steam_lib.SteamAPI_ISteamUGC_SetReturnAdditionalPreviews.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetReturnAdditionalPreviews.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetReturnTotalOnly

steam_lib.SteamAPI_ISteamUGC_SetReturnTotalOnly.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetReturnTotalOnly.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetReturnPlaytimeStats

steam_lib.SteamAPI_ISteamUGC_SetReturnPlaytimeStats.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetReturnPlaytimeStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetLanguage

steam_lib.SteamAPI_ISteamUGC_SetLanguage.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetLanguage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetAllowCachedResponse

steam_lib.SteamAPI_ISteamUGC_SetAllowCachedResponse.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetAllowCachedResponse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetAdminQuery

steam_lib.SteamAPI_ISteamUGC_SetAdminQuery.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetAdminQuery.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetCloudFileNameFilter

steam_lib.SteamAPI_ISteamUGC_SetCloudFileNameFilter.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetCloudFileNameFilter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetMatchAnyTag

steam_lib.SteamAPI_ISteamUGC_SetMatchAnyTag.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetMatchAnyTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetSearchText

steam_lib.SteamAPI_ISteamUGC_SetSearchText.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetSearchText.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetRankedByTrendDays

steam_lib.SteamAPI_ISteamUGC_SetRankedByTrendDays.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetRankedByTrendDays.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetTimeCreatedDateRange

steam_lib.SteamAPI_ISteamUGC_SetTimeCreatedDateRange.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetTimeCreatedDateRange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetTimeUpdatedDateRange

steam_lib.SteamAPI_ISteamUGC_SetTimeUpdatedDateRange.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetTimeUpdatedDateRange.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddRequiredKeyValueTag

steam_lib.SteamAPI_ISteamUGC_AddRequiredKeyValueTag.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_AddRequiredKeyValueTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_RequestUGCDetails

steam_lib.SteamAPI_ISteamUGC_RequestUGCDetails.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_RequestUGCDetails.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_CreateItem

steam_lib.SteamAPI_ISteamUGC_CreateItem.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_CreateItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_StartItemUpdate

steam_lib.SteamAPI_ISteamUGC_StartItemUpdate.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_StartItemUpdate.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetItemTitle

steam_lib.SteamAPI_ISteamUGC_SetItemTitle.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetItemTitle.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetItemDescription

steam_lib.SteamAPI_ISteamUGC_SetItemDescription.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetItemDescription.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetItemUpdateLanguage

steam_lib.SteamAPI_ISteamUGC_SetItemUpdateLanguage.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetItemUpdateLanguage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetItemMetadata

steam_lib.SteamAPI_ISteamUGC_SetItemMetadata.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetItemMetadata.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetItemVisibility

steam_lib.SteamAPI_ISteamUGC_SetItemVisibility.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetItemVisibility.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetItemTags

steam_lib.SteamAPI_ISteamUGC_SetItemTags.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetItemTags.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetItemContent

steam_lib.SteamAPI_ISteamUGC_SetItemContent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetItemContent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetItemPreview

steam_lib.SteamAPI_ISteamUGC_SetItemPreview.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetItemPreview.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetAllowLegacyUpload

steam_lib.SteamAPI_ISteamUGC_SetAllowLegacyUpload.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetAllowLegacyUpload.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_RemoveAllItemKeyValueTags

steam_lib.SteamAPI_ISteamUGC_RemoveAllItemKeyValueTags.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_RemoveAllItemKeyValueTags.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_RemoveItemKeyValueTags

steam_lib.SteamAPI_ISteamUGC_RemoveItemKeyValueTags.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_RemoveItemKeyValueTags.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddItemKeyValueTag

steam_lib.SteamAPI_ISteamUGC_AddItemKeyValueTag.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_AddItemKeyValueTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddItemPreviewFile

steam_lib.SteamAPI_ISteamUGC_AddItemPreviewFile.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_AddItemPreviewFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddItemPreviewVideo

steam_lib.SteamAPI_ISteamUGC_AddItemPreviewVideo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_AddItemPreviewVideo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_UpdateItemPreviewFile

steam_lib.SteamAPI_ISteamUGC_UpdateItemPreviewFile.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_UpdateItemPreviewFile.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_UpdateItemPreviewVideo

steam_lib.SteamAPI_ISteamUGC_UpdateItemPreviewVideo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_UpdateItemPreviewVideo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_RemoveItemPreview

steam_lib.SteamAPI_ISteamUGC_RemoveItemPreview.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_RemoveItemPreview.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddContentDescriptor

steam_lib.SteamAPI_ISteamUGC_AddContentDescriptor.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_AddContentDescriptor.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_RemoveContentDescriptor

steam_lib.SteamAPI_ISteamUGC_RemoveContentDescriptor.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_RemoveContentDescriptor.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetRequiredGameVersions

steam_lib.SteamAPI_ISteamUGC_SetRequiredGameVersions.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SetRequiredGameVersions.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SubmitItemUpdate

steam_lib.SteamAPI_ISteamUGC_SubmitItemUpdate.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_SubmitItemUpdate.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetItemUpdateProgress

steam_lib.SteamAPI_ISteamUGC_GetItemUpdateProgress.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_GetItemUpdateProgress.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SetUserItemVote

steam_lib.SteamAPI_ISteamUGC_SetUserItemVote.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SetUserItemVote.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetUserItemVote

steam_lib.SteamAPI_ISteamUGC_GetUserItemVote.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetUserItemVote.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddItemToFavorites

steam_lib.SteamAPI_ISteamUGC_AddItemToFavorites.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_AddItemToFavorites.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_RemoveItemFromFavorites

steam_lib.SteamAPI_ISteamUGC_RemoveItemFromFavorites.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_RemoveItemFromFavorites.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SubscribeItem

steam_lib.SteamAPI_ISteamUGC_SubscribeItem.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SubscribeItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_UnsubscribeItem

steam_lib.SteamAPI_ISteamUGC_UnsubscribeItem.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_UnsubscribeItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetNumSubscribedItems

steam_lib.SteamAPI_ISteamUGC_GetNumSubscribedItems.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_GetNumSubscribedItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetSubscribedItems

steam_lib.SteamAPI_ISteamUGC_GetSubscribedItems.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetSubscribedItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetItemState

steam_lib.SteamAPI_ISteamUGC_GetItemState.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetItemState.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetItemInstallInfo

steam_lib.SteamAPI_ISteamUGC_GetItemInstallInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_GetItemInstallInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetItemDownloadInfo

steam_lib.SteamAPI_ISteamUGC_GetItemDownloadInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_GetItemDownloadInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_DownloadItem

steam_lib.SteamAPI_ISteamUGC_DownloadItem.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_DownloadItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_BInitWorkshopForGameServer

steam_lib.SteamAPI_ISteamUGC_BInitWorkshopForGameServer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_BInitWorkshopForGameServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_SuspendDownloads

steam_lib.SteamAPI_ISteamUGC_SuspendDownloads.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_SuspendDownloads.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_StartPlaytimeTracking

steam_lib.SteamAPI_ISteamUGC_StartPlaytimeTracking.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_StartPlaytimeTracking.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_StopPlaytimeTracking

steam_lib.SteamAPI_ISteamUGC_StopPlaytimeTracking.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_StopPlaytimeTracking.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_StopPlaytimeTrackingForAllItems

steam_lib.SteamAPI_ISteamUGC_StopPlaytimeTrackingForAllItems.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_StopPlaytimeTrackingForAllItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddDependency

steam_lib.SteamAPI_ISteamUGC_AddDependency.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_AddDependency.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_RemoveDependency

steam_lib.SteamAPI_ISteamUGC_RemoveDependency.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_RemoveDependency.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_AddAppDependency

steam_lib.SteamAPI_ISteamUGC_AddAppDependency.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_AddAppDependency.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_RemoveAppDependency

steam_lib.SteamAPI_ISteamUGC_RemoveAppDependency.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_RemoveAppDependency.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetAppDependencies

steam_lib.SteamAPI_ISteamUGC_GetAppDependencies.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetAppDependencies.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_DeleteItem

steam_lib.SteamAPI_ISteamUGC_DeleteItem.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_DeleteItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_ShowWorkshopEULA

steam_lib.SteamAPI_ISteamUGC_ShowWorkshopEULA.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_ShowWorkshopEULA.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetWorkshopEULAStatus

steam_lib.SteamAPI_ISteamUGC_GetWorkshopEULAStatus.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamUGC_GetWorkshopEULAStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamUGC_GetUserContentDescriptorPreferences

steam_lib.SteamAPI_ISteamUGC_GetUserContentDescriptorPreferences.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamUGC_GetUserContentDescriptorPreferences.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_Init

steam_lib.SteamAPI_ISteamHTMLSurface_Init.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTMLSurface_Init.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_Shutdown

steam_lib.SteamAPI_ISteamHTMLSurface_Shutdown.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTMLSurface_Shutdown.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_CreateBrowser

steam_lib.SteamAPI_ISteamHTMLSurface_CreateBrowser.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTMLSurface_CreateBrowser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_RemoveBrowser

steam_lib.SteamAPI_ISteamHTMLSurface_RemoveBrowser.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_RemoveBrowser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_LoadURL

steam_lib.SteamAPI_ISteamHTMLSurface_LoadURL.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTMLSurface_LoadURL.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_SetSize

steam_lib.SteamAPI_ISteamHTMLSurface_SetSize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_SetSize.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_StopLoad

steam_lib.SteamAPI_ISteamHTMLSurface_StopLoad.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_StopLoad.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_Reload

steam_lib.SteamAPI_ISteamHTMLSurface_Reload.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_Reload.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_GoBack

steam_lib.SteamAPI_ISteamHTMLSurface_GoBack.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_GoBack.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_GoForward

steam_lib.SteamAPI_ISteamHTMLSurface_GoForward.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_GoForward.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_AddHeader

steam_lib.SteamAPI_ISteamHTMLSurface_AddHeader.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTMLSurface_AddHeader.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_ExecuteJavascript

steam_lib.SteamAPI_ISteamHTMLSurface_ExecuteJavascript.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTMLSurface_ExecuteJavascript.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_MouseUp

steam_lib.SteamAPI_ISteamHTMLSurface_MouseUp.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_MouseUp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_MouseDown

steam_lib.SteamAPI_ISteamHTMLSurface_MouseDown.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_MouseDown.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_MouseDoubleClick

steam_lib.SteamAPI_ISteamHTMLSurface_MouseDoubleClick.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_MouseDoubleClick.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_MouseMove

steam_lib.SteamAPI_ISteamHTMLSurface_MouseMove.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_MouseMove.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_MouseWheel

steam_lib.SteamAPI_ISteamHTMLSurface_MouseWheel.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_MouseWheel.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_KeyDown

steam_lib.SteamAPI_ISteamHTMLSurface_KeyDown.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_KeyDown.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_KeyUp

steam_lib.SteamAPI_ISteamHTMLSurface_KeyUp.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_KeyUp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_KeyChar

steam_lib.SteamAPI_ISteamHTMLSurface_KeyChar.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_KeyChar.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_SetHorizontalScroll

steam_lib.SteamAPI_ISteamHTMLSurface_SetHorizontalScroll.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_SetHorizontalScroll.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_SetVerticalScroll

steam_lib.SteamAPI_ISteamHTMLSurface_SetVerticalScroll.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_SetVerticalScroll.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_SetKeyFocus

steam_lib.SteamAPI_ISteamHTMLSurface_SetKeyFocus.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_SetKeyFocus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_ViewSource

steam_lib.SteamAPI_ISteamHTMLSurface_ViewSource.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_ViewSource.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_CopyToClipboard

steam_lib.SteamAPI_ISteamHTMLSurface_CopyToClipboard.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_CopyToClipboard.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_PasteFromClipboard

steam_lib.SteamAPI_ISteamHTMLSurface_PasteFromClipboard.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_PasteFromClipboard.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_Find

steam_lib.SteamAPI_ISteamHTMLSurface_Find.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_Find.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_StopFind

steam_lib.SteamAPI_ISteamHTMLSurface_StopFind.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_StopFind.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_GetLinkAtPosition

steam_lib.SteamAPI_ISteamHTMLSurface_GetLinkAtPosition.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_GetLinkAtPosition.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_SetCookie

steam_lib.SteamAPI_ISteamHTMLSurface_SetCookie.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_SetCookie.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_SetPageScaleFactor

steam_lib.SteamAPI_ISteamHTMLSurface_SetPageScaleFactor.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_SetPageScaleFactor.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_SetBackgroundMode

steam_lib.SteamAPI_ISteamHTMLSurface_SetBackgroundMode.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_SetBackgroundMode.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_SetDPIScalingFactor

steam_lib.SteamAPI_ISteamHTMLSurface_SetDPIScalingFactor.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_SetDPIScalingFactor.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_OpenDeveloperTools

steam_lib.SteamAPI_ISteamHTMLSurface_OpenDeveloperTools.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_OpenDeveloperTools.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_AllowStartRequest

steam_lib.SteamAPI_ISteamHTMLSurface_AllowStartRequest.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_AllowStartRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_JSDialogResponse

steam_lib.SteamAPI_ISteamHTMLSurface_JSDialogResponse.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamHTMLSurface_JSDialogResponse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamHTMLSurface_FileLoadDialogResponse

steam_lib.SteamAPI_ISteamHTMLSurface_FileLoadDialogResponse.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamHTMLSurface_FileLoadDialogResponse.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetResultStatus

steam_lib.SteamAPI_ISteamInventory_GetResultStatus.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_GetResultStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetResultItems

steam_lib.SteamAPI_ISteamInventory_GetResultItems.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GetResultItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetResultItemProperty

steam_lib.SteamAPI_ISteamInventory_GetResultItemProperty.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GetResultItemProperty.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetResultTimestamp

steam_lib.SteamAPI_ISteamInventory_GetResultTimestamp.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_GetResultTimestamp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_CheckResultSteamID

steam_lib.SteamAPI_ISteamInventory_CheckResultSteamID.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_CheckResultSteamID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_DestroyResult

steam_lib.SteamAPI_ISteamInventory_DestroyResult.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_DestroyResult.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetAllItems

steam_lib.SteamAPI_ISteamInventory_GetAllItems.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GetAllItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetItemsByID

steam_lib.SteamAPI_ISteamInventory_GetItemsByID.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_GetItemsByID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_SerializeResult

steam_lib.SteamAPI_ISteamInventory_SerializeResult.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_SerializeResult.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_DeserializeResult

steam_lib.SteamAPI_ISteamInventory_DeserializeResult.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_DeserializeResult.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GenerateItems

steam_lib.SteamAPI_ISteamInventory_GenerateItems.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_GenerateItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GrantPromoItems

steam_lib.SteamAPI_ISteamInventory_GrantPromoItems.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GrantPromoItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_AddPromoItem

steam_lib.SteamAPI_ISteamInventory_AddPromoItem.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_AddPromoItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_AddPromoItems

steam_lib.SteamAPI_ISteamInventory_AddPromoItems.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_AddPromoItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_ConsumeItem

steam_lib.SteamAPI_ISteamInventory_ConsumeItem.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_ConsumeItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_ExchangeItems

steam_lib.SteamAPI_ISteamInventory_ExchangeItems.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_ExchangeItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_TransferItemQuantity

steam_lib.SteamAPI_ISteamInventory_TransferItemQuantity.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_TransferItemQuantity.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_SendItemDropHeartbeat

steam_lib.SteamAPI_ISteamInventory_SendItemDropHeartbeat.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_SendItemDropHeartbeat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_TriggerItemDrop

steam_lib.SteamAPI_ISteamInventory_TriggerItemDrop.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_TriggerItemDrop.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_TradeItems

steam_lib.SteamAPI_ISteamInventory_TradeItems.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_TradeItems.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_LoadItemDefinitions

steam_lib.SteamAPI_ISteamInventory_LoadItemDefinitions.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_LoadItemDefinitions.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetItemDefinitionIDs

steam_lib.SteamAPI_ISteamInventory_GetItemDefinitionIDs.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GetItemDefinitionIDs.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetItemDefinitionProperty

steam_lib.SteamAPI_ISteamInventory_GetItemDefinitionProperty.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GetItemDefinitionProperty.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_RequestEligiblePromoItemDefinitionsIDs

steam_lib.SteamAPI_ISteamInventory_RequestEligiblePromoItemDefinitionsIDs.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_RequestEligiblePromoItemDefinitionsIDs.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetEligiblePromoItemDefinitionIDs

steam_lib.SteamAPI_ISteamInventory_GetEligiblePromoItemDefinitionIDs.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GetEligiblePromoItemDefinitionIDs.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_StartPurchase

steam_lib.SteamAPI_ISteamInventory_StartPurchase.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_StartPurchase.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_RequestPrices

steam_lib.SteamAPI_ISteamInventory_RequestPrices.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_RequestPrices.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetNumItemsWithPrices

steam_lib.SteamAPI_ISteamInventory_GetNumItemsWithPrices.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GetNumItemsWithPrices.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetItemsWithPrices

steam_lib.SteamAPI_ISteamInventory_GetItemsWithPrices.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_GetItemsWithPrices.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_GetItemPrice

steam_lib.SteamAPI_ISteamInventory_GetItemPrice.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_GetItemPrice.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_StartUpdateProperties

steam_lib.SteamAPI_ISteamInventory_StartUpdateProperties.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_StartUpdateProperties.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_RemoveProperty

steam_lib.SteamAPI_ISteamInventory_RemoveProperty.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_RemoveProperty.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_SetPropertyString

steam_lib.SteamAPI_ISteamInventory_SetPropertyString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_SetPropertyString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_SetPropertyBool

steam_lib.SteamAPI_ISteamInventory_SetPropertyBool.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_SetPropertyBool.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_SetPropertyInt64

steam_lib.SteamAPI_ISteamInventory_SetPropertyInt64.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_SetPropertyInt64.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_SetPropertyFloat

steam_lib.SteamAPI_ISteamInventory_SetPropertyFloat.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamInventory_SetPropertyFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_SubmitUpdateProperties

steam_lib.SteamAPI_ISteamInventory_SubmitUpdateProperties.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_SubmitUpdateProperties.restype = ctypes.c_int


# Binding for SteamAPI_ISteamInventory_InspectItem

steam_lib.SteamAPI_ISteamInventory_InspectItem.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamInventory_InspectItem.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_SetTimelineTooltip

steam_lib.SteamAPI_ISteamTimeline_SetTimelineTooltip.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_SetTimelineTooltip.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_ClearTimelineTooltip

steam_lib.SteamAPI_ISteamTimeline_ClearTimelineTooltip.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_ClearTimelineTooltip.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_SetTimelineGameMode

steam_lib.SteamAPI_ISteamTimeline_SetTimelineGameMode.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_SetTimelineGameMode.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_AddInstantaneousTimelineEvent

steam_lib.SteamAPI_ISteamTimeline_AddInstantaneousTimelineEvent.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_AddInstantaneousTimelineEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_AddRangeTimelineEvent

steam_lib.SteamAPI_ISteamTimeline_AddRangeTimelineEvent.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_AddRangeTimelineEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_StartRangeTimelineEvent

steam_lib.SteamAPI_ISteamTimeline_StartRangeTimelineEvent.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_StartRangeTimelineEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_UpdateRangeTimelineEvent

steam_lib.SteamAPI_ISteamTimeline_UpdateRangeTimelineEvent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_UpdateRangeTimelineEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_EndRangeTimelineEvent

steam_lib.SteamAPI_ISteamTimeline_EndRangeTimelineEvent.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_EndRangeTimelineEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_RemoveTimelineEvent

steam_lib.SteamAPI_ISteamTimeline_RemoveTimelineEvent.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_RemoveTimelineEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_DoesEventRecordingExist

steam_lib.SteamAPI_ISteamTimeline_DoesEventRecordingExist.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_DoesEventRecordingExist.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_StartGamePhase

steam_lib.SteamAPI_ISteamTimeline_StartGamePhase.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamTimeline_StartGamePhase.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_EndGamePhase

steam_lib.SteamAPI_ISteamTimeline_EndGamePhase.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamTimeline_EndGamePhase.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_SetGamePhaseID

steam_lib.SteamAPI_ISteamTimeline_SetGamePhaseID.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamTimeline_SetGamePhaseID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_DoesGamePhaseRecordingExist

steam_lib.SteamAPI_ISteamTimeline_DoesGamePhaseRecordingExist.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamTimeline_DoesGamePhaseRecordingExist.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_AddGamePhaseTag

steam_lib.SteamAPI_ISteamTimeline_AddGamePhaseTag.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_AddGamePhaseTag.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_SetGamePhaseAttribute

steam_lib.SteamAPI_ISteamTimeline_SetGamePhaseAttribute.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_SetGamePhaseAttribute.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_OpenOverlayToGamePhase

steam_lib.SteamAPI_ISteamTimeline_OpenOverlayToGamePhase.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamTimeline_OpenOverlayToGamePhase.restype = ctypes.c_int


# Binding for SteamAPI_ISteamTimeline_OpenOverlayToTimelineEvent

steam_lib.SteamAPI_ISteamTimeline_OpenOverlayToTimelineEvent.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamTimeline_OpenOverlayToTimelineEvent.restype = ctypes.c_int


# Binding for SteamAPI_ISteamVideo_GetVideoURL

steam_lib.SteamAPI_ISteamVideo_GetVideoURL.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamVideo_GetVideoURL.restype = ctypes.c_int


# Binding for SteamAPI_ISteamVideo_IsBroadcasting

steam_lib.SteamAPI_ISteamVideo_IsBroadcasting.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamVideo_IsBroadcasting.restype = ctypes.c_int


# Binding for SteamAPI_ISteamVideo_GetOPFSettings

steam_lib.SteamAPI_ISteamVideo_GetOPFSettings.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamVideo_GetOPFSettings.restype = ctypes.c_int


# Binding for SteamAPI_ISteamVideo_GetOPFStringForApp

steam_lib.SteamAPI_ISteamVideo_GetOPFStringForApp.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamVideo_GetOPFStringForApp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParentalSettings_BIsParentalLockEnabled

steam_lib.SteamAPI_ISteamParentalSettings_BIsParentalLockEnabled.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamParentalSettings_BIsParentalLockEnabled.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParentalSettings_BIsParentalLockLocked

steam_lib.SteamAPI_ISteamParentalSettings_BIsParentalLockLocked.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamParentalSettings_BIsParentalLockLocked.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParentalSettings_BIsAppBlocked

steam_lib.SteamAPI_ISteamParentalSettings_BIsAppBlocked.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParentalSettings_BIsAppBlocked.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParentalSettings_BIsAppInBlockList

steam_lib.SteamAPI_ISteamParentalSettings_BIsAppInBlockList.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParentalSettings_BIsAppInBlockList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParentalSettings_BIsFeatureBlocked

steam_lib.SteamAPI_ISteamParentalSettings_BIsFeatureBlocked.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParentalSettings_BIsFeatureBlocked.restype = ctypes.c_int


# Binding for SteamAPI_ISteamParentalSettings_BIsFeatureInBlockList

steam_lib.SteamAPI_ISteamParentalSettings_BIsFeatureInBlockList.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamParentalSettings_BIsFeatureInBlockList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemotePlay_GetSessionCount

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemotePlay_GetSessionID

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionID.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemotePlay_GetSessionSteamID

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionSteamID.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionSteamID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemotePlay_GetSessionClientName

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionClientName.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionClientName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemotePlay_GetSessionClientFormFactor

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionClientFormFactor.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemotePlay_GetSessionClientFormFactor.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemotePlay_BGetSessionClientResolution

steam_lib.SteamAPI_ISteamRemotePlay_BGetSessionClientResolution.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamRemotePlay_BGetSessionClientResolution.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemotePlay_BStartRemotePlayTogether

steam_lib.SteamAPI_ISteamRemotePlay_BStartRemotePlayTogether.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemotePlay_BStartRemotePlayTogether.restype = ctypes.c_int


# Binding for SteamAPI_ISteamRemotePlay_BSendRemotePlayTogetherInvite

steam_lib.SteamAPI_ISteamRemotePlay_BSendRemotePlayTogetherInvite.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamRemotePlay_BSendRemotePlayTogetherInvite.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingMessages_SendMessageToUser

steam_lib.SteamAPI_ISteamNetworkingMessages_SendMessageToUser.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingMessages_SendMessageToUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingMessages_ReceiveMessagesOnChannel

steam_lib.SteamAPI_ISteamNetworkingMessages_ReceiveMessagesOnChannel.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingMessages_ReceiveMessagesOnChannel.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingMessages_AcceptSessionWithUser

steam_lib.SteamAPI_ISteamNetworkingMessages_AcceptSessionWithUser.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingMessages_AcceptSessionWithUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingMessages_CloseSessionWithUser

steam_lib.SteamAPI_ISteamNetworkingMessages_CloseSessionWithUser.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingMessages_CloseSessionWithUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingMessages_CloseChannelWithUser

steam_lib.SteamAPI_ISteamNetworkingMessages_CloseChannelWithUser.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingMessages_CloseChannelWithUser.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingMessages_GetSessionConnectionInfo

steam_lib.SteamAPI_ISteamNetworkingMessages_GetSessionConnectionInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingMessages_GetSessionConnectionInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CreateListenSocketIP

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateListenSocketIP.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateListenSocketIP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ConnectByIPAddress

steam_lib.SteamAPI_ISteamNetworkingSockets_ConnectByIPAddress.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_ConnectByIPAddress.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2P

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2P.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2P.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ConnectP2P

steam_lib.SteamAPI_ISteamNetworkingSockets_ConnectP2P.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_ConnectP2P.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_AcceptConnection

steam_lib.SteamAPI_ISteamNetworkingSockets_AcceptConnection.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_AcceptConnection.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CloseConnection

steam_lib.SteamAPI_ISteamNetworkingSockets_CloseConnection.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_CloseConnection.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CloseListenSocket

steam_lib.SteamAPI_ISteamNetworkingSockets_CloseListenSocket.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_CloseListenSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_SetConnectionUserData

steam_lib.SteamAPI_ISteamNetworkingSockets_SetConnectionUserData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_SetConnectionUserData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetConnectionUserData

steam_lib.SteamAPI_ISteamNetworkingSockets_GetConnectionUserData.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetConnectionUserData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_SetConnectionName

steam_lib.SteamAPI_ISteamNetworkingSockets_SetConnectionName.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_SetConnectionName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetConnectionName

steam_lib.SteamAPI_ISteamNetworkingSockets_GetConnectionName.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetConnectionName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_SendMessageToConnection

steam_lib.SteamAPI_ISteamNetworkingSockets_SendMessageToConnection.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_SendMessageToConnection.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_SendMessages

steam_lib.SteamAPI_ISteamNetworkingSockets_SendMessages.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_SendMessages.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_FlushMessagesOnConnection

steam_lib.SteamAPI_ISteamNetworkingSockets_FlushMessagesOnConnection.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_FlushMessagesOnConnection.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnConnection

steam_lib.SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnConnection.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnConnection.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetConnectionInfo

steam_lib.SteamAPI_ISteamNetworkingSockets_GetConnectionInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetConnectionInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetConnectionRealTimeStatus

steam_lib.SteamAPI_ISteamNetworkingSockets_GetConnectionRealTimeStatus.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetConnectionRealTimeStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetDetailedConnectionStatus

steam_lib.SteamAPI_ISteamNetworkingSockets_GetDetailedConnectionStatus.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetDetailedConnectionStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetListenSocketAddress

steam_lib.SteamAPI_ISteamNetworkingSockets_GetListenSocketAddress.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetListenSocketAddress.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CreateSocketPair

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateSocketPair.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateSocketPair.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ConfigureConnectionLanes

steam_lib.SteamAPI_ISteamNetworkingSockets_ConfigureConnectionLanes.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_ConfigureConnectionLanes.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetIdentity

steam_lib.SteamAPI_ISteamNetworkingSockets_GetIdentity.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetIdentity.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_InitAuthentication

steam_lib.SteamAPI_ISteamNetworkingSockets_InitAuthentication.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_InitAuthentication.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetAuthenticationStatus

steam_lib.SteamAPI_ISteamNetworkingSockets_GetAuthenticationStatus.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetAuthenticationStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CreatePollGroup

steam_lib.SteamAPI_ISteamNetworkingSockets_CreatePollGroup.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_CreatePollGroup.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_DestroyPollGroup

steam_lib.SteamAPI_ISteamNetworkingSockets_DestroyPollGroup.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_DestroyPollGroup.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_SetConnectionPollGroup

steam_lib.SteamAPI_ISteamNetworkingSockets_SetConnectionPollGroup.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_SetConnectionPollGroup.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnPollGroup

steam_lib.SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnPollGroup.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_ReceiveMessagesOnPollGroup.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ReceivedRelayAuthTicket

steam_lib.SteamAPI_ISteamNetworkingSockets_ReceivedRelayAuthTicket.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_ReceivedRelayAuthTicket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_FindRelayAuthTicketForServer

steam_lib.SteamAPI_ISteamNetworkingSockets_FindRelayAuthTicketForServer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_FindRelayAuthTicketForServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ConnectToHostedDedicatedServer

steam_lib.SteamAPI_ISteamNetworkingSockets_ConnectToHostedDedicatedServer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_ConnectToHostedDedicatedServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPort

steam_lib.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPort.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPort.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPOPID

steam_lib.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPOPID.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerPOPID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerAddress

steam_lib.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerAddress.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetHostedDedicatedServerAddress.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateHostedDedicatedServerListenSocket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetGameCoordinatorServerLogin

steam_lib.SteamAPI_ISteamNetworkingSockets_GetGameCoordinatorServerLogin.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetGameCoordinatorServerLogin.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ConnectP2PCustomSignaling

steam_lib.SteamAPI_ISteamNetworkingSockets_ConnectP2PCustomSignaling.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_ConnectP2PCustomSignaling.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ReceivedP2PCustomSignal

steam_lib.SteamAPI_ISteamNetworkingSockets_ReceivedP2PCustomSignal.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_ReceivedP2PCustomSignal.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetCertificateRequest

steam_lib.SteamAPI_ISteamNetworkingSockets_GetCertificateRequest.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetCertificateRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_SetCertificate

steam_lib.SteamAPI_ISteamNetworkingSockets_SetCertificate.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_SetCertificate.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_ResetIdentity

steam_lib.SteamAPI_ISteamNetworkingSockets_ResetIdentity.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_ResetIdentity.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_RunCallbacks

steam_lib.SteamAPI_ISteamNetworkingSockets_RunCallbacks.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_RunCallbacks.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_BeginAsyncRequestFakeIP

steam_lib.SteamAPI_ISteamNetworkingSockets_BeginAsyncRequestFakeIP.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_BeginAsyncRequestFakeIP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetFakeIP

steam_lib.SteamAPI_ISteamNetworkingSockets_GetFakeIP.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetFakeIP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2PFakeIP

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2PFakeIP.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateListenSocketP2PFakeIP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_GetRemoteFakeIPForConnection

steam_lib.SteamAPI_ISteamNetworkingSockets_GetRemoteFakeIPForConnection.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingSockets_GetRemoteFakeIPForConnection.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingSockets_CreateFakeUDPPort

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateFakeUDPPort.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingSockets_CreateFakeUDPPort.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_AllocateMessage

steam_lib.SteamAPI_ISteamNetworkingUtils_AllocateMessage.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_AllocateMessage.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_InitRelayNetworkAccess

steam_lib.SteamAPI_ISteamNetworkingUtils_InitRelayNetworkAccess.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_InitRelayNetworkAccess.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetRelayNetworkStatus

steam_lib.SteamAPI_ISteamNetworkingUtils_GetRelayNetworkStatus.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetRelayNetworkStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetLocalPingLocation

steam_lib.SteamAPI_ISteamNetworkingUtils_GetLocalPingLocation.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetLocalPingLocation.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations

steam_lib.SteamAPI_ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_EstimatePingTimeBetweenTwoLocations.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_EstimatePingTimeFromLocalHost

steam_lib.SteamAPI_ISteamNetworkingUtils_EstimatePingTimeFromLocalHost.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_EstimatePingTimeFromLocalHost.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_ConvertPingLocationToString

steam_lib.SteamAPI_ISteamNetworkingUtils_ConvertPingLocationToString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_ConvertPingLocationToString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_ParsePingLocationString

steam_lib.SteamAPI_ISteamNetworkingUtils_ParsePingLocationString.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_ParsePingLocationString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_CheckPingDataUpToDate

steam_lib.SteamAPI_ISteamNetworkingUtils_CheckPingDataUpToDate.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_CheckPingDataUpToDate.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetPingToDataCenter

steam_lib.SteamAPI_ISteamNetworkingUtils_GetPingToDataCenter.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetPingToDataCenter.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetDirectPingToPOP

steam_lib.SteamAPI_ISteamNetworkingUtils_GetDirectPingToPOP.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetDirectPingToPOP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetPOPCount

steam_lib.SteamAPI_ISteamNetworkingUtils_GetPOPCount.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetPOPCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetPOPList

steam_lib.SteamAPI_ISteamNetworkingUtils_GetPOPList.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetPOPList.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetLocalTimestamp

steam_lib.SteamAPI_ISteamNetworkingUtils_GetLocalTimestamp.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetLocalTimestamp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetDebugOutputFunction

steam_lib.SteamAPI_ISteamNetworkingUtils_SetDebugOutputFunction.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetDebugOutputFunction.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_IsFakeIPv4

steam_lib.SteamAPI_ISteamNetworkingUtils_IsFakeIPv4.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_IsFakeIPv4.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetIPv4FakeIPType

steam_lib.SteamAPI_ISteamNetworkingUtils_GetIPv4FakeIPType.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetIPv4FakeIPType.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetRealIdentityForFakeIP

steam_lib.SteamAPI_ISteamNetworkingUtils_GetRealIdentityForFakeIP.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetRealIdentityForFakeIP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueInt32

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueInt32.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueInt32.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueFloat

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueFloat.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueString

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValueString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValuePtr

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValuePtr.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalConfigValuePtr.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueInt32

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueInt32.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueInt32.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueFloat

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueFloat.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueString

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConnectionConfigValueString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetConnectionStatusChanged.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamNetAuthenticationStatusChanged.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_SteamRelayNetworkStatusChanged.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_FakeIPResult.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionRequest.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetGlobalCallback_MessagesSessionFailed.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetConfigValue

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConfigValue.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConfigValue.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SetConfigValueStruct

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConfigValueStruct.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SetConfigValueStruct.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetConfigValue

steam_lib.SteamAPI_ISteamNetworkingUtils_GetConfigValue.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetConfigValue.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_GetConfigValueInfo

steam_lib.SteamAPI_ISteamNetworkingUtils_GetConfigValueInfo.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_GetConfigValueInfo.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_IterateGenericEditableConfigValues

steam_lib.SteamAPI_ISteamNetworkingUtils_IterateGenericEditableConfigValues.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_IterateGenericEditableConfigValues.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ToString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_ParseString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIPAddr_GetFakeIPType.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ToString

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ToString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ToString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingUtils_SteamNetworkingIdentity_ParseString.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetProduct

steam_lib.SteamAPI_ISteamGameServer_SetProduct.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetProduct.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetGameDescription

steam_lib.SteamAPI_ISteamGameServer_SetGameDescription.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetGameDescription.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetModDir

steam_lib.SteamAPI_ISteamGameServer_SetModDir.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetModDir.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetDedicatedServer

steam_lib.SteamAPI_ISteamGameServer_SetDedicatedServer.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_SetDedicatedServer.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_LogOn

steam_lib.SteamAPI_ISteamGameServer_LogOn.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_LogOn.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_LogOnAnonymous

steam_lib.SteamAPI_ISteamGameServer_LogOnAnonymous.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_LogOnAnonymous.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_LogOff

steam_lib.SteamAPI_ISteamGameServer_LogOff.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_LogOff.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_BLoggedOn

steam_lib.SteamAPI_ISteamGameServer_BLoggedOn.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_BLoggedOn.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_BSecure

steam_lib.SteamAPI_ISteamGameServer_BSecure.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_BSecure.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_GetSteamID

steam_lib.SteamAPI_ISteamGameServer_GetSteamID.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_GetSteamID.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_WasRestartRequested

steam_lib.SteamAPI_ISteamGameServer_WasRestartRequested.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_WasRestartRequested.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetMaxPlayerCount

steam_lib.SteamAPI_ISteamGameServer_SetMaxPlayerCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_SetMaxPlayerCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetBotPlayerCount

steam_lib.SteamAPI_ISteamGameServer_SetBotPlayerCount.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_SetBotPlayerCount.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetServerName

steam_lib.SteamAPI_ISteamGameServer_SetServerName.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetServerName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetMapName

steam_lib.SteamAPI_ISteamGameServer_SetMapName.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetMapName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetPasswordProtected

steam_lib.SteamAPI_ISteamGameServer_SetPasswordProtected.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_SetPasswordProtected.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetSpectatorPort

steam_lib.SteamAPI_ISteamGameServer_SetSpectatorPort.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_SetSpectatorPort.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetSpectatorServerName

steam_lib.SteamAPI_ISteamGameServer_SetSpectatorServerName.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetSpectatorServerName.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_ClearAllKeyValues

steam_lib.SteamAPI_ISteamGameServer_ClearAllKeyValues.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_ClearAllKeyValues.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetKeyValue

steam_lib.SteamAPI_ISteamGameServer_SetKeyValue.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetKeyValue.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetGameTags

steam_lib.SteamAPI_ISteamGameServer_SetGameTags.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetGameTags.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetGameData

steam_lib.SteamAPI_ISteamGameServer_SetGameData.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetGameData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetRegion

steam_lib.SteamAPI_ISteamGameServer_SetRegion.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SetRegion.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SetAdvertiseServerActive

steam_lib.SteamAPI_ISteamGameServer_SetAdvertiseServerActive.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_SetAdvertiseServerActive.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_GetAuthSessionTicket

steam_lib.SteamAPI_ISteamGameServer_GetAuthSessionTicket.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_GetAuthSessionTicket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_BeginAuthSession

steam_lib.SteamAPI_ISteamGameServer_BeginAuthSession.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_BeginAuthSession.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_EndAuthSession

steam_lib.SteamAPI_ISteamGameServer_EndAuthSession.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_EndAuthSession.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_CancelAuthTicket

steam_lib.SteamAPI_ISteamGameServer_CancelAuthTicket.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_CancelAuthTicket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_UserHasLicenseForApp

steam_lib.SteamAPI_ISteamGameServer_UserHasLicenseForApp.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_UserHasLicenseForApp.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_RequestUserGroupStatus

steam_lib.SteamAPI_ISteamGameServer_RequestUserGroupStatus.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_RequestUserGroupStatus.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_GetGameplayStats

steam_lib.SteamAPI_ISteamGameServer_GetGameplayStats.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_GetGameplayStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_GetServerReputation

steam_lib.SteamAPI_ISteamGameServer_GetServerReputation.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_GetServerReputation.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_GetPublicIP

steam_lib.SteamAPI_ISteamGameServer_GetPublicIP.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_GetPublicIP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_HandleIncomingPacket

steam_lib.SteamAPI_ISteamGameServer_HandleIncomingPacket.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_HandleIncomingPacket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_GetNextOutgoingPacket

steam_lib.SteamAPI_ISteamGameServer_GetNextOutgoingPacket.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_GetNextOutgoingPacket.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_AssociateWithClan

steam_lib.SteamAPI_ISteamGameServer_AssociateWithClan.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_AssociateWithClan.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_ComputeNewPlayerCompatibility

steam_lib.SteamAPI_ISteamGameServer_ComputeNewPlayerCompatibility.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_ComputeNewPlayerCompatibility.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED

steam_lib.SteamAPI_ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_SendUserConnectAndAuthenticate_DEPRECATED.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_CreateUnauthenticatedUserConnection

steam_lib.SteamAPI_ISteamGameServer_CreateUnauthenticatedUserConnection.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServer_CreateUnauthenticatedUserConnection.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_SendUserDisconnect_DEPRECATED

steam_lib.SteamAPI_ISteamGameServer_SendUserDisconnect_DEPRECATED.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_SendUserDisconnect_DEPRECATED.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServer_BUpdateUserData

steam_lib.SteamAPI_ISteamGameServer_BUpdateUserData.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServer_BUpdateUserData.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_RequestUserStats

steam_lib.SteamAPI_ISteamGameServerStats_RequestUserStats.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServerStats_RequestUserStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_GetUserStatInt32

steam_lib.SteamAPI_ISteamGameServerStats_GetUserStatInt32.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServerStats_GetUserStatInt32.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_GetUserStatFloat

steam_lib.SteamAPI_ISteamGameServerStats_GetUserStatFloat.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServerStats_GetUserStatFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_GetUserAchievement

steam_lib.SteamAPI_ISteamGameServerStats_GetUserAchievement.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServerStats_GetUserAchievement.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_SetUserStatInt32

steam_lib.SteamAPI_ISteamGameServerStats_SetUserStatInt32.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServerStats_SetUserStatInt32.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_SetUserStatFloat

steam_lib.SteamAPI_ISteamGameServerStats_SetUserStatFloat.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServerStats_SetUserStatFloat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_UpdateUserAvgRateStat

steam_lib.SteamAPI_ISteamGameServerStats_UpdateUserAvgRateStat.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServerStats_UpdateUserAvgRateStat.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_SetUserAchievement

steam_lib.SteamAPI_ISteamGameServerStats_SetUserAchievement.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServerStats_SetUserAchievement.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_ClearUserAchievement

steam_lib.SteamAPI_ISteamGameServerStats_ClearUserAchievement.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_ISteamGameServerStats_ClearUserAchievement.restype = ctypes.c_int


# Binding for SteamAPI_ISteamGameServerStats_StoreUserStats

steam_lib.SteamAPI_ISteamGameServerStats_StoreUserStats.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamGameServerStats_StoreUserStats.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort

steam_lib.SteamAPI_ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_ISteamNetworkingFakeUDPPort_DestroyFakeUDPPort.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingFakeUDPPort_SendMessageToFakeIP

steam_lib.SteamAPI_ISteamNetworkingFakeUDPPort_SendMessageToFakeIP.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingFakeUDPPort_SendMessageToFakeIP.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingFakeUDPPort_ReceiveMessages

steam_lib.SteamAPI_ISteamNetworkingFakeUDPPort_ReceiveMessages.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingFakeUDPPort_ReceiveMessages.restype = ctypes.c_int


# Binding for SteamAPI_ISteamNetworkingFakeUDPPort_ScheduleCleanup

steam_lib.SteamAPI_ISteamNetworkingFakeUDPPort_ScheduleCleanup.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_ISteamNetworkingFakeUDPPort_ScheduleCleanup.restype = ctypes.c_int


# Binding for SteamAPI_SteamIPAddress_t_IsSet

steam_lib.SteamAPI_SteamIPAddress_t_IsSet.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamIPAddress_t_IsSet.restype = ctypes.c_int


# Binding for SteamAPI_MatchMakingKeyValuePair_t_Construct

steam_lib.SteamAPI_MatchMakingKeyValuePair_t_Construct.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_MatchMakingKeyValuePair_t_Construct.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_Construct

steam_lib.SteamAPI_servernetadr_t_Construct.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_servernetadr_t_Construct.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_Init

steam_lib.SteamAPI_servernetadr_t_Init.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_servernetadr_t_Init.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_GetQueryPort

steam_lib.SteamAPI_servernetadr_t_GetQueryPort.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_servernetadr_t_GetQueryPort.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_SetQueryPort

steam_lib.SteamAPI_servernetadr_t_SetQueryPort.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_servernetadr_t_SetQueryPort.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_GetConnectionPort

steam_lib.SteamAPI_servernetadr_t_GetConnectionPort.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_servernetadr_t_GetConnectionPort.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_SetConnectionPort

steam_lib.SteamAPI_servernetadr_t_SetConnectionPort.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_servernetadr_t_SetConnectionPort.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_GetIP

steam_lib.SteamAPI_servernetadr_t_GetIP.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_servernetadr_t_GetIP.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_SetIP

steam_lib.SteamAPI_servernetadr_t_SetIP.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_servernetadr_t_SetIP.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_GetConnectionAddressString

steam_lib.SteamAPI_servernetadr_t_GetConnectionAddressString.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_servernetadr_t_GetConnectionAddressString.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_GetQueryAddressString

steam_lib.SteamAPI_servernetadr_t_GetQueryAddressString.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_servernetadr_t_GetQueryAddressString.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_IsLessThan

steam_lib.SteamAPI_servernetadr_t_IsLessThan.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_servernetadr_t_IsLessThan.restype = ctypes.c_int


# Binding for SteamAPI_servernetadr_t_Assign

steam_lib.SteamAPI_servernetadr_t_Assign.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_servernetadr_t_Assign.restype = ctypes.c_int


# Binding for SteamAPI_gameserveritem_t_Construct

steam_lib.SteamAPI_gameserveritem_t_Construct.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_gameserveritem_t_Construct.restype = ctypes.c_int


# Binding for SteamAPI_gameserveritem_t_GetName

steam_lib.SteamAPI_gameserveritem_t_GetName.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_gameserveritem_t_GetName.restype = ctypes.c_int


# Binding for SteamAPI_gameserveritem_t_SetName

steam_lib.SteamAPI_gameserveritem_t_SetName.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_gameserveritem_t_SetName.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_Clear

steam_lib.SteamAPI_SteamNetworkingIPAddr_Clear.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIPAddr_Clear.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_IsIPv6AllZeros

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsIPv6AllZeros.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsIPv6AllZeros.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_SetIPv6

steam_lib.SteamAPI_SteamNetworkingIPAddr_SetIPv6.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIPAddr_SetIPv6.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_SetIPv4

steam_lib.SteamAPI_SteamNetworkingIPAddr_SetIPv4.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIPAddr_SetIPv4.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_IsIPv4

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsIPv4.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsIPv4.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_GetIPv4

steam_lib.SteamAPI_SteamNetworkingIPAddr_GetIPv4.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIPAddr_GetIPv4.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_SetIPv6LocalHost

steam_lib.SteamAPI_SteamNetworkingIPAddr_SetIPv6LocalHost.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIPAddr_SetIPv6LocalHost.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_IsLocalHost

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsLocalHost.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsLocalHost.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_ToString

steam_lib.SteamAPI_SteamNetworkingIPAddr_ToString.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIPAddr_ToString.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_ParseString

steam_lib.SteamAPI_SteamNetworkingIPAddr_ParseString.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIPAddr_ParseString.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_IsEqualTo

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsEqualTo.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsEqualTo.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_GetFakeIPType

steam_lib.SteamAPI_SteamNetworkingIPAddr_GetFakeIPType.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIPAddr_GetFakeIPType.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIPAddr_IsFakeIP

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsFakeIP.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIPAddr_IsFakeIP.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_Clear

steam_lib.SteamAPI_SteamNetworkingIdentity_Clear.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_Clear.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_IsInvalid

steam_lib.SteamAPI_SteamNetworkingIdentity_IsInvalid.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_IsInvalid.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetSteamID

steam_lib.SteamAPI_SteamNetworkingIdentity_SetSteamID.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetSteamID.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetSteamID

steam_lib.SteamAPI_SteamNetworkingIdentity_GetSteamID.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetSteamID.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetSteamID64

steam_lib.SteamAPI_SteamNetworkingIdentity_SetSteamID64.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetSteamID64.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetSteamID64

steam_lib.SteamAPI_SteamNetworkingIdentity_GetSteamID64.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetSteamID64.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetXboxPairwiseID

steam_lib.SteamAPI_SteamNetworkingIdentity_SetXboxPairwiseID.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetXboxPairwiseID.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetXboxPairwiseID

steam_lib.SteamAPI_SteamNetworkingIdentity_GetXboxPairwiseID.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetXboxPairwiseID.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetPSNID

steam_lib.SteamAPI_SteamNetworkingIdentity_SetPSNID.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetPSNID.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetPSNID

steam_lib.SteamAPI_SteamNetworkingIdentity_GetPSNID.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetPSNID.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetIPAddr

steam_lib.SteamAPI_SteamNetworkingIdentity_SetIPAddr.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetIPAddr.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetIPAddr

steam_lib.SteamAPI_SteamNetworkingIdentity_GetIPAddr.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetIPAddr.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetIPv4Addr

steam_lib.SteamAPI_SteamNetworkingIdentity_SetIPv4Addr.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetIPv4Addr.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetIPv4

steam_lib.SteamAPI_SteamNetworkingIdentity_GetIPv4.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetIPv4.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetFakeIPType

steam_lib.SteamAPI_SteamNetworkingIdentity_GetFakeIPType.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetFakeIPType.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_IsFakeIP

steam_lib.SteamAPI_SteamNetworkingIdentity_IsFakeIP.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_IsFakeIP.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetLocalHost

steam_lib.SteamAPI_SteamNetworkingIdentity_SetLocalHost.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetLocalHost.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_IsLocalHost

steam_lib.SteamAPI_SteamNetworkingIdentity_IsLocalHost.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_IsLocalHost.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetGenericString

steam_lib.SteamAPI_SteamNetworkingIdentity_SetGenericString.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetGenericString.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetGenericString

steam_lib.SteamAPI_SteamNetworkingIdentity_GetGenericString.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetGenericString.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_SetGenericBytes

steam_lib.SteamAPI_SteamNetworkingIdentity_SetGenericBytes.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_SetGenericBytes.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_GetGenericBytes

steam_lib.SteamAPI_SteamNetworkingIdentity_GetGenericBytes.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_GetGenericBytes.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_IsEqualTo

steam_lib.SteamAPI_SteamNetworkingIdentity_IsEqualTo.argtypes = [ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_IsEqualTo.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_ToString

steam_lib.SteamAPI_SteamNetworkingIdentity_ToString.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingIdentity_ToString.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingIdentity_ParseString

steam_lib.SteamAPI_SteamNetworkingIdentity_ParseString.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingIdentity_ParseString.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingMessage_t_Release

steam_lib.SteamAPI_SteamNetworkingMessage_t_Release.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingMessage_t_Release.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingConfigValue_t_SetInt32

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetInt32.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetInt32.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingConfigValue_t_SetInt64

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetInt64.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetInt64.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingConfigValue_t_SetFloat

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetFloat.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetFloat.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingConfigValue_t_SetPtr

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetPtr.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetPtr.restype = ctypes.c_int


# Binding for SteamAPI_SteamNetworkingConfigValue_t_SetString

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetString.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

steam_lib.SteamAPI_SteamNetworkingConfigValue_t_SetString.restype = ctypes.c_int


# Binding for SteamAPI_SteamDatagramHostedAddress_Clear

steam_lib.SteamAPI_SteamDatagramHostedAddress_Clear.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamDatagramHostedAddress_Clear.restype = ctypes.c_int


# Binding for SteamAPI_SteamDatagramHostedAddress_GetPopID

steam_lib.SteamAPI_SteamDatagramHostedAddress_GetPopID.argtypes = [ctypes.c_void_p]

steam_lib.SteamAPI_SteamDatagramHostedAddress_GetPopID.restype = ctypes.c_int


# Binding for SteamAPI_SteamDatagramHostedAddress_SetDevAddress

steam_lib.SteamAPI_SteamDatagramHostedAddress_SetDevAddress.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]

steam_lib.SteamAPI_SteamDatagramHostedAddress_SetDevAddress.restype = ctypes.c_int

