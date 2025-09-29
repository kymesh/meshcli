from typing import Callable
from weakref import ref as WeakRef
from weakrefmethod import WeakMethod

WeakObjOrMethod = WeakMethod | WeakRef
DeadRefObserver = Callable[[WeakObjOrMethod], None]

def getWeakRef(obj, notifyDead: DeadRefObserver = None): ...
