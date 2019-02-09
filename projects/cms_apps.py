from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ProjectsApphook(CMSApp):
    app_name = "projects"  # must match the application namespace
    name = "Projects App"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["projects.urls"] # replace this with the path to your application's URLs module