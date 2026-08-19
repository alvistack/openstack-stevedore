=====================
 Resolving Conflicts
=====================

.. versionadded:: 5.6.0

Entry point names do not have to be unique within a namespace. This is
intentional and is what makes the *hooks* pattern (:doc:`patterns_loading`)
possible, where several entry points share a name so that they can all be
invoked for a single event. For the *drivers* pattern, however, a name is
expected to identify exactly one implementation, and for the *extensions*
pattern each name is used to look up a single extension. When more than one
entry point in a namespace registers under the same name, stevedore has to
decide which one to use. This is a *conflict*, and the mechanism that decides
what to do about it is the *conflict resolver*.

Conflicts most commonly arise when two packages are installed that both
provide a plugin under the same name in the same namespace. For example, two
libraries that each register a ``sqlite`` driver in the ``myapp.database``
namespace.

The ``conflict_resolver`` parameter
===================================

The following managers accept a ``conflict_resolver`` keyword argument:

* :class:`~stevedore.extension.ExtensionManager`
* :class:`~stevedore.named.NamedExtensionManager`
* :class:`~stevedore.driver.DriverManager`

A conflict resolver is any callable matching
:data:`~stevedore.extension.ConflictResolverT`. It is called with three
arguments - the namespace, the conflicting name, and the list of
:class:`~stevedore.extension.Extension` objects that share that name - and must
return the single :class:`~stevedore.extension.Extension` to use (or raise an
exception to abort):

.. code-block:: python

    def resolver(namespace, name, entrypoints):
        # return one of the entries in ``entrypoints``
        ...

The resolver is only consulted for name-based lookups. For the
:class:`~stevedore.extension.ExtensionManager` and
:class:`~stevedore.named.NamedExtensionManager` this happens lazily, the first
time an extension is retrieved by name. For the
:class:`~stevedore.driver.DriverManager`, which always loads a single named
driver, it is consulted when the manager is constructed.

Built-in resolvers
==================

stevedore ships with two resolvers, both in the :mod:`stevedore.extension`
module.

:func:`~stevedore.extension.ignore_conflicts`
    Logs a warning listing the conflicting implementations and returns the last
    entry point found, so a single plugin is selected and no error is raised.
    This is the default for :class:`~stevedore.extension.ExtensionManager` and
    :class:`~stevedore.named.NamedExtensionManager`.

:func:`~stevedore.extension.error_on_conflict`
    Raises :class:`~stevedore.exception.MultipleMatches`, refusing to resolve
    the conflict silently. This is the default for
    :class:`~stevedore.driver.DriverManager`.

.. versionchanged:: 5.9.1

   Prior to 5.9.1, :class:`~stevedore.driver.DriverManager` unconditionally
   raised :class:`~stevedore.exception.MultipleMatches` and ignored any
   ``conflict_resolver`` that was passed. Since 5.9.1 this parameter is
   honoured and defaults to :func:`~stevedore.extension.error_on_conflict` to
   preserve the historical "raise on duplicate" behavior.

Usage
=====

To have a :class:`~stevedore.driver.DriverManager` pick a driver instead of
raising when duplicates are present, pass
:func:`~stevedore.extension.ignore_conflicts`:

.. code-block:: python

    from stevedore import driver
    from stevedore import extension

    mgr = driver.DriverManager(
        namespace='myapp.database',
        name='sqlite',
        invoke_on_load=True,
        conflict_resolver=extension.ignore_conflicts,
    )

Alternatively, to make an :class:`~stevedore.extension.ExtensionManager` or
:class:`~stevedore.named.NamedExtensionManager` raise on duplicates rather than
silently choosing one, pass :func:`~stevedore.extension.error_on_conflict`:

.. code-block:: python

    from stevedore import extension

    mgr = extension.ExtensionManager(
        namespace='myapp.formatters',
        conflict_resolver=extension.error_on_conflict,
    )

Writing a custom resolver
=========================

When neither built-in resolver expresses the policy you need, you can provide
your own callable. This can be useful if you want to prefer an implementation
from a particular package, for example. The example below prefers the first
entry point discovered:

.. code-block:: python

    from stevedore import driver

    def prefer_first(namespace, name, entrypoints):
        return entrypoints[0]

    mgr = driver.DriverManager(
        namespace='myapp.database',
        name='sqlite',
        invoke_on_load=True,
        conflict_resolver=prefer_first,
    )

A custom resolver may also raise an exception to reject the conflict, just as
:func:`~stevedore.extension.error_on_conflict` does.

.. seealso::

   * :doc:`patterns_loading`
   * :class:`stevedore.driver.DriverManager`
   * :class:`stevedore.extension.ExtensionManager`
   * :class:`stevedore.named.NamedExtensionManager`
