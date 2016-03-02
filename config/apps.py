from suit.apps import DjangoSuitConfig


class DjangoSuit(DjangoSuitConfig):

    admin_name = 'Work the Election API Admin'

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
            'label': 'Application & Surveys',
            'models': (
                'survey.application',
                'survey.survey',
            )
        },
        {
            'label': 'Pages',
            'models': (
                'pages.page',
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
