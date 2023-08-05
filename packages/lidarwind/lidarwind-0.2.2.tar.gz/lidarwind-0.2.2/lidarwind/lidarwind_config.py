"""Module for configuring the data global attribute

"""

import json


class Configurations:
    """Global attributes definition

    This class defines all global attributes
    that will be writen on the dataset

    Parameters
    ----------
    lidarwind : object
        an instance of the lidarwind package

    """

    def __init__(self, lidarwind=None):

        self.load_version(lidarwind)
        self.load_reference()
        self.load_institution()
        self.load_instrument()
        self.load_site()
        self.load_contact()
        self.load_email()
        self.load_comments()

    def load_version(self, lidarwind):
        """
        It identifies the lidarwind version
        and writes it to the configuration file

        Parameters
        ----------
        lidarwind : object
            a instance of the lidarwind package

        """

        if lidarwind is None:
            self.lidarwind_version = "temporary config file"
        else:
            self.lidarwind_version = lidarwind.__version__

        return self

    def load_institution(self, institution="institution name"):
        """
        It defines the institution affiliation name

        Parameters
        ----------
        institution : str
            institution name

        """

        self.institution = institution

        return self

    def load_instrument(self, instrument="instrument name"):
        """
        It defines the instrument name

        Parameters
        ----------
        instrument : str
            name of the instrument used during the experiment

        """

        self.instrument = instrument

        return self

    def load_site(self, site="site name"):
        """
        It defines the name of the experimental site

        Parameters
        ----------
        site : str
            name of the experimental site

        """

        self.site = site

        return self

    def load_contact(self, contact="contact person"):
        """
        It defines the author's name

        Parameters
        ----------
        contact : str
            name of the contact person

        """

        self.contact = contact

        return self

    def load_email(self, email="contact email"):
        """
        It defines the contacting email

        Parameters
        ----------
        email : str
            contact email

        """
        self.email = email

        return self

    def load_reference(self, reference="Generated by lidarwind version: {0}"):
        """
        It loads the lidarwind's version used for
        processing the data

        Parameters
        ----------
        reference : str
            lidarwind version used to process the data

        """

        self.references = reference.format(self.lidarwind_version)

        return self

    def load_comments(self, comments="General comments"):
        """
        It defines additional comments

        Parameters
        ----------
        comments : str
            additional comments

        """
        self.comments = comments

        return self

    def generate_conf(self):
        """
        It writes and saves all defined global attributes.

        """

        config_dic = {}

        config_dic["references"] = self.references
        config_dic["institution"] = self.institution
        config_dic["instrument_name"] = self.instrument
        config_dic["site_name"] = self.site
        config_dic["comments"] = self.comments
        config_dic["contact_person"] = self.contact
        config_dic["email"] = self.email

        config_js = json.dumps(config_dic)
        config_file = open("config.json", "w")
        config_file.write(config_js)
        config_file.close()

    def load_conf_file(self, file_path="config.json"):
        """
        It loads the pre-defined global attributes
        from the config.json, if it exists.

        Parameters
        ----------
        file_path : str
            the path to the configuration file (config.json)

        """

        try:
            config_dic = json.load(open(file_path))

        except FileNotFoundError:

            print("You do not have a config file yet")
            print("a temporary config file was generated")
            print("See the documentation for generating it")
            self.generate_conf()
            config_dic = json.load(open(file_path))

        self.load_reference(config_dic["references"])
        self.load_institution(config_dic["institution"])
        self.load_instrument(config_dic["instrument_name"])
        self.load_comments(config_dic["comments"])
        self.load_site(config_dic["site_name"])
        self.load_contact(config_dic["contact_person"])
        self.load_email(config_dic["email"])

        return self
