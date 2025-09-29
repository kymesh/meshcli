from ..core.topictreetraverser import ITopicTreeVisitor as ITopicTreeVisitor, TopicTreeTraverser as TopicTreeTraverser
from _typeshed import Incomplete
from typing import TextIO

class TopicTreePrinter(ITopicTreeVisitor):
    allowedExtras: Incomplete
    ALL_TOPICS_NAME: str
    def __init__(self, extra=None, width: int = 70, indentStep: int = 4, bulletTopic: str = '\\--', bulletTopicItem: str = '|==', bulletTopicArg: str = '-', fileObj: TextIO = None) -> None: ...
    def getOutput(self): ...

def printTreeDocs(rootTopic=None, topicMgr=None, **kwargs) -> None: ...
