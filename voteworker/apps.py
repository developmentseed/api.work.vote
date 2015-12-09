from suit.apps import DjangoSuitConfig


class DjangoSuit(DjangoSuitConfig):

    admin_name = 'VoteWorker'

    list_per_page = 50

    menu = (
        # Rename app and set icon
        {
            'label': 'States',
            'models': (
                'jurisdiction.state',
            )
        },
        {
            'label': 'Jurisdictions',
            'models': (
                'jurisdiction.jurisdiction',
            )
        },
        {
            'label': 'Users & Groups',
            'models': (
                'auth.user',
                'auth.group',
            )
        }
    )
