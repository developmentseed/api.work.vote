from suit.apps import DjangoSuitConfig


class DjangoSuit(DjangoSuitConfig):

    admin_name = 'VoteWorker'

    list_per_page = 50

    menu = (
            # Rename app and set icon
        )
