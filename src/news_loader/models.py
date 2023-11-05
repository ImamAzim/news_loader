import os
import shutil


import xdg


CONFIG_FP = os.path.join(os.path.dirname(__file__), 'config', 'config.toml')

class NewsCreator(object):

    """contains tools to fetch news, merge to an epub and upload it"""

    def __init__(self):
        """TODO: to be defined. """
        pass

    def create_config_file(self, overwrite=False):
        """create a config file of news_loader for current user

        :overwrite: True is you want to overwrite previous config

        """
        directory = os.path.join(xdg.XDG_CONFIG_HOME, 'news_loader')
        if not os.path.exists(directory):
            os.makedirs(directory)

        path = os.path.join(directory, 'config.toml')
        if os.path.exists(path) and not overwrite:
            raise FileExistsError
        else:
            shutil.copy(CONFIG_FP, path)


class NewsLoaderConfiguration(object):

    """class to set configuration of the news loader app"""

    def __init__(self):
        """initiate and create dict config and path to file"""
        self._config_dict = dict(
                recipes=dict(),
                comics_rss_feeds=list(),
                )

        directory = os.path.join(xdg.XDG_CONFIG_HOME, 'news_loader')
        if not os.path.exists(directory):
            os.makedirs(directory)

        self.config_fp = os.path.join(directory, 'config.toml')

    def get_recipes_names(self):
        """find present custom recipes in calibre config folder
        :returns: list of recipes names, path to custom_recipe

        """
        folder_path = os.path.join(xdg.XDG_CONFIG_HOME, 'calibre', 'custom_recipes')
        if not os.path.exists(folder_path):
            return [], folder_path
        else:
            files = os.listdir(folder_path)
            recipes = [
                    filename[0:-len('.recipe')]
                    for filename in files if filename.split('.')[-1] == 'recipe']
            return recipes, folder_path

    def add_recipe(self, recipe_name, username=None, password=None):
        """add a recipe to the config dict

        :recipe_name: name that match a custom recipe
        :username: str if required
        :password: str if required

        """
        self._config_dict['recipes'][recipe_name] = dict(
                username=username,
                password=password,,
                )

    def add_comics_rss(self, rss_link: str):
        """add a rss feed of a comics

        :rss_link: valid url of a feed

        """
        pass

    def add_nextcloud_config(self, webdav_link: str, username: str, password: str):
        """add nextcloud ocnfig toconfig

        :webdav_link: TODO
        :username: TODO
        :password: TODO
        :returns: TODO

        """
        pass

    def save_config(self, overwrite=False):
        """TODO: Docstring for save_config.

        :overwrite: TODO
        :returns: TODO

        """
        pass

    def delete_config(self):
        """TODO: Docstring for delete_config.
        :returns: TODO

        """
        pass

    def add_crontab(self, arg1):
        """TODO: Docstring for add_crontab.

        :arg1: TODO
        :returns: TODO

        """
        pass

    def del_crontab(self, arg1):
        """TODO: Docstring for del_crontab.

        :arg1: TODO
        :returns: TODO

        """
        pass


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    pass
