===============
 API Reference
===============

Extension Manager Classes
=========================

DriverManager
-------------

.. autoclass:: stevedore.driver.DriverManager

HookManager
-----------

.. autoclass:: stevedore.hook.HookManager

NamedExtensionManager
---------------------

.. autoclass:: stevedore.named.NamedExtensionManager

EnabledExtensionManager
-----------------------

.. autoclass:: stevedore.enabled.EnabledExtensionManager

DispatchExtensionManager
------------------------

.. autoclass:: stevedore.dispatch.DispatchExtensionManager

NameDispatchExtensionManager
----------------------------

.. autoclass:: stevedore.dispatch.NameDispatchExtensionManager

ExtensionManager
----------------

.. autoclass:: stevedore.extension.ExtensionManager

Extension
---------

.. autoclass:: stevedore.extension.Extension
   :members:
   :show-inheritance:
   :no-special-members:

Conflict Resolution
===================

See :doc:`../user/conflict_resolution` for an overview of how conflicting
entry point names are resolved.

.. autodata:: stevedore.extension.ConflictResolverT

.. autofunction:: stevedore.extension.ignore_conflicts

.. autofunction:: stevedore.extension.error_on_conflict

Exceptions
==========

.. autoexception:: stevedore.exception.NoUniqueMatch

.. autoexception:: stevedore.exception.NoMatches

.. autoexception:: stevedore.exception.MultipleMatches
