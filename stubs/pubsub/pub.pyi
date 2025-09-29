from .core import ALL_TOPICS as ALL_TOPICS, AUTO_TOPIC as AUTO_TOPIC, ExcHandlerError as ExcHandlerError, IListenerExcHandler as IListenerExcHandler, ListenerMismatchError as ListenerMismatchError, TOPIC_TREE_FROM_CLASS as TOPIC_TREE_FROM_CLASS, TOPIC_TREE_FROM_MODULE as TOPIC_TREE_FROM_MODULE, TOPIC_TREE_FROM_STRING as TOPIC_TREE_FROM_STRING, Topic as Topic, TopicManager as TopicManager, TopicNameError as TopicNameError, TopicTreeTraverser as TopicTreeTraverser, exportTopicTreeSpec as exportTopicTreeSpec
from _typeshed import Incomplete

__all__ = ['subscribe', 'unsubscribe', 'unsubAll', 'isSubscribed', 'isValid', 'validate', 'ListenerMismatchError', 'AUTO_TOPIC', 'IListenerExcHandler', 'getListenerExcHandler', 'setListenerExcHandler', 'ExcHandlerError', 'ALL_TOPICS', 'Topic', 'topicTreeRoot', 'topicsMap', 'TopicManager', 'getDefaultTopicMgr', 'addTopicDefnProvider', 'clearTopicDefnProviders', 'getNumTopicDefnProviders', 'TOPIC_TREE_FROM_MODULE', 'TOPIC_TREE_FROM_CLASS', 'TOPIC_TREE_FROM_STRING', 'exportTopicTreeSpec', 'instantiateAllDefinedTopicsTopicDefnError', 'TopicNameError', 'setTopicUnspecifiedFatal', 'sendMessage', 'addNotificationHandler', 'setNotificationFlags', 'getNotificationFlags', 'clearNotificationHandlers', 'TopicTreeTraverser']

subscribe: Incomplete
unsubscribe: Incomplete
unsubAll: Incomplete
sendMessage: Incomplete
getListenerExcHandler: Incomplete
setListenerExcHandler: Incomplete
addNotificationHandler: Incomplete
clearNotificationHandlers: Incomplete
setNotificationFlags: Incomplete
getNotificationFlags: Incomplete
setTopicUnspecifiedFatal: Incomplete
topicTreeRoot: Incomplete
topicsMap: Incomplete

def isValid(listener, topicName, curriedArgNames=None) -> bool: ...
def validate(listener, topicName, curriedArgNames=None) -> None: ...
def isSubscribed(listener, topicName) -> bool: ...
def getDefaultTopicMgr() -> TopicManager: ...

addTopicDefnProvider: Incomplete
clearTopicDefnProviders: Incomplete
getNumTopicDefnProviders: Incomplete

# Names in __all__ with no definition:
#   instantiateAllDefinedTopicsTopicDefnError
