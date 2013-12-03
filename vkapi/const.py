# -*- coding: utf-8 -*-

# version 5.5

API_URL = 'https://api.vk.com/method/'

PUBLIC_METHODS = ['utils.getServerTime']

FATAL_ERROR_CODES = [5, 14, 16, 17, 3]

ERRORS = {5: u'User authorization failed: no access_token passed.',
          14: u'Captcha needed',
          16: u'HTTP authorization failed',
          17: u'Validation required ',
          3: u'Unknown method passed'
          }

METHOD_SECTIONS = ['secure', 'wall', 'apps', 'utils', 'video', 'likes',
                   'stats', 'ads', 'storage', 'board', 'widgets', 'status',
                   'users', 'database', 'docs', 'fave', 'search', 'auth',
                   'photos', 'groups', 'friends', 'pages', 'account',
                   'places', 'notifications', 'notes', 'polls', 'messages',
                   'newsfeed', 'audio', 'execute']

ALL_METHODS = [
    'users.get', 'users.search', 'users.isAppUser', 'users.getSubscriptions', 'users.getFollowers', 'users.report',
    'groups.isMember', 'groups.getById', 'groups.get', 'groups.getMembers', 'groups.join', 'groups.leave', 'groups.search', 'groups.getInvites', 'groups.banUser', 'groups.unbanUser', 'groups.getBanned',
    'friends.get', 'friends.getOnline', 'friends.getMutual', 'friends.getRecent', 'friends.getRequests', 'friends.add', 'friends.edit', 'friends.delete', 'friends.getLists', 'friends.addList', 'friends.editList', 'friends.deleteList', 'friends.getAppUsers', 'friends.getByPhones', 'friends.deleteAllRequests', 'friends.getSuggestions', 'friends.areFriends',
    'wall.get', 'wall.getById', 'wall.savePost', 'wall.post', 'wall.repost', 'wall.getReposts', 'wall.edit', 'wall.delete', 'wall.restore', 'wall.getComments', 'wall.addComment', 'wall.editComment', 'wall.deleteComment', 'wall.restoreComment',
    'photos.createAlbum', 'photos.editAlbum', 'photos.getAlbums', 'photos.get', 'photos.getAlbumsCount', 'photos.getProfile', 'photos.getById', 'photos.getUploadServer', 'photos.getProfileUploadServer', 'photos.getChatUploadServer', 'photos.saveProfilePhoto', 'photos.saveWallPhoto', 'photos.getWallUploadServer', 'photos.getMessagesUploadServer', 'photos.saveMessagesPhoto', 'photos.search', 'photos.save', 'photos.copy', 'photos.edit', 'photos.move', 'photos.makeCover', 'photos.reorderAlbums', 'photos.reorderPhotos', 'photos.getAll', 'photos.getUserPhotos', 'photos.deleteAlbum', 'photos.delete', 'photos.confirmTag', 'photos.getComments', 'photos.getAllComments', 'photos.createComment', 'photos.deleteComment', 'photos.restoreComment', 'photos.editComment', 'photos.getTags', 'photos.putTag', 'photos.removeTag', 'photos.getNewTags',
    'video.get', 'video.edit', 'video.add', 'video.save', 'video.delete', 'video.restore', 'video.search', 'video.getUserVideos', 'video.getAlbums', 'video.addAlbum', 'video.editAlbum', 'video.deleteAlbum', 'video.moveToAlbum', 'video.getComments', 'video.createComment', 'video.deleteComment', 'video.restoreComment', 'video.editComment', 'video.getTags', 'video.putTag', 'video.removeTag', 'video.getNewTags', 'video.report',
    'audio.get', 'audio.getById', 'audio.getLyrics', 'audio.search', 'audio.getUploadServer', 'audio.save', 'audio.add', 'audio.delete', 'audio.edit', 'audio.reorder', 'audio.restore', 'audio.getAlbums', 'audio.addAlbum', 'audio.editAlbum', 'audio.deleteAlbum', 'audio.moveToAlbum', 'audio.setBroadcast', 'audio.getBroadcastList', 'audio.getRecommendations', 'audio.getPopular', 'audio.getCount',
    'messages.get', 'messages.getDialogs', 'messages.getById', 'messages.search', 'messages.getHistory', 'messages.send', 'messages.delete', 'messages.deleteDialog', 'messages.restore', 'messages.markAsNew', 'messages.markAsRead', 'messages.markAsImportant', 'messages.getLongPollServer', 'messages.getLongPollHistory', 'messages.getChat', 'messages.createChat', 'messages.editChat', 'messages.getChatUsers', 'messages.setActivity', 'messages.searchDialogs', 'messages.addChatUser', 'messages.removeChatUser', 'messages.getLastActivity', 'messages.setChatPhoto', 'messages.deleteChatPhoto',
    'newsfeed.get', 'newsfeed.getRecommended', 'newsfeed.getComments', 'newsfeed.getMentions', 'newsfeed.getBanned', 'newsfeed.addBan', 'newsfeed.deleteBan', 'newsfeed.search', 'newsfeed.getLists', 'newsfeed.unsubscribe', 'newsfeed.getSuggestedSources',
    'likes.getList', 'likes.add', 'likes.delete', 'likes.isLiked',
    'storage.get', 'storage.set',
    'account.getCounters', 'account.setNameInMenu', 'account.setOnline', 'account.setOffline', 'account.lookupContacts', 'account.registerDevice', 'account.unregisterDevice', 'account.setSilenceMode', 'account.getPushSettings', 'account.getAppPermissions', 'account.getActiveOffers', 'account.banUser', 'account.unbanUser', 'account.getBanned', 'account.getInfo', 'account.setInfo',
    'auth.checkPhone', 'auth.signup', 'auth.confirm',
    'widgets.getComments', 'widgets.getPages',
    'secure.getAppBalance', 'secure.getTransactionsHistory', 'secure.getSMSHistory', 'secure.sendSMSNotification', 'secure.sendNotification', 'secure.setCounter', 'secure.setUserLevel', 'secure.getUserLevel', 'secure.checkToken',
    'status.get', 'status.set',
    'pages.get', 'pages.save', 'pages.saveAccess', 'pages.getHistory', 'pages.getTitles', 'pages.getVersion', 'pages.parseWiki', 'pages.clearCache',
    'board.getTopics', 'board.getComments', 'board.addTopic', 'board.addComment', 'board.deleteTopic', 'board.editTopic', 'board.editComment', 'board.restoreComment', 'board.deleteComment', 'board.openTopic', 'board.closeTopic', 'board.fixTopic', 'board.unfixTopic',
    'notes.get', 'notes.getById', 'notes.getFriendsNotes', 'notes.add', 'notes.edit', 'notes.delete', 'notes.getComments', 'notes.createComment', 'notes.editComment', 'notes.deleteComment', 'notes.restoreComment',
    'places.add', 'places.getById', 'places.search', 'places.checkin', 'places.getCheckins', 'places.getTypes',
    'polls.getById', 'polls.addVote', 'polls.deleteVote', 'polls.getVoters',
    'docs.get', 'docs.getById', 'docs.getUploadServer', 'docs.getWallUploadServer', 'docs.save', 'docs.delete', 'docs.add',
    'fave.getUsers', 'fave.getPhotos', 'fave.getPosts', 'fave.getVideos', 'fave.getLinks',
    'notifications.get', 'notifications.markAsViewed',
    'stats.get',
    'search.getHints',
    'apps.getCatalog',
    'utils.checkLink', 'utils.resolveScreenName', 'utils.getServerTime',
    'database.getCountries', 'database.getRegions', 'database.getStreetsById', 'database.getCountriesById', 'database.getCities', 'database.getCitiesById', 'database.getUniversities', 'database.getSchools', 'database.getFaculties',
    'ads.getAccounts', 'ads.getClients', 'ads.createClients', 'ads.updateClients', 'ads.deleteClients', 'ads.getCampaigns', 'ads.createCampaigns', 'ads.updateCampaigns', 'ads.deleteCampaigns', 'ads.getAds', 'ads.getAdsLayout', 'ads.getAdsTargeting', 'ads.createAds', 'ads.updateAds', 'ads.deleteAds', 'ads.getStatistics', 'ads.getDemographics', 'ads.getBudget', 'ads.getOfficeUsers', 'ads.addOfficeUsers', 'ads.removeOfficeUsers', 'ads.getTargetingStats', 'ads.getSuggestions', 'ads.getCategories', 'ads.getUploadURL', 'ads.getVideoUploadURL', 'ads.getFloodStats', 'ads.getRejectionReason', 'ads.createTargetGroup', 'ads.updateTargetGroup', 'ads.deleteTargetGroup', 'ads.getTargetGroups', 'ads.importTargetContacts',
    'execute']
