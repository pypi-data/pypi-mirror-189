import os

def out_source_is_self(uow):
    # Use this filter in listeners to not consume events my service just emitted
    return (
        not 'tags' in uow['event'] or
        uow['event']['tags']['source'] != os.getenv('SERVICE')
    )

def out_latched(uow):
    # Use this filter in triggers to not emit events in reaction to an update from a listener
    # listeners should set latched = true
    # commands/mutations should set latched = null
    return (
        # create & update latch
        (uow['event']['raw']['new'] and not uow['event']['raw']['new']['latched'])
        # delete latch
        or (not uow['event']['raw']['new'] and uow['event']['raw']['old']
            and not uow['event']['raw']['old']['latched'])
        )
