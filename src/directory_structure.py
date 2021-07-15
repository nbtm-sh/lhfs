import os

class DirectoryStructure:
    def __init__(self):
        self.directories = []
    
    def list_directory(path, effective_user = "nouser", effective_group = "nogroup"):
        paths = [fd for fd in path.split("/")] # Split paths without removing tailing forward slash

class DirectoryMapping:
    def __init__(self):
        self.real_path = ""
        self.virtual_path = ""

        self.creation_user = ""
        self.create_date = ""
        self.modify_date = ""
                                                # Unauthenticated user can list and read by default
        self.permissions = [DirectoryPermission("nouser", "nogroup", True, True, False)]
    
    def has_list_permission(self, effective_user=None, effective_group=None):


class DirectoryPermission:
    def __init__(self, username, group, per_list, per_read, per_write):
        self.username = username
        self.group = group

        # Read, write and view permissions for directory
        self.per_list = per_list # List files
        self.per_read = per_read # Read contents of files
        self.per_write = per_write # Write new files/modify contents of existing files
    
    def match(self, ef_user, ef_group):
        """ Returns True if either the group or the user match """
        match = True

        if ef_user != None:
            match = self.username == ef_user
        
        if ef_group != None:
            match &= self.group == ef_group
        
        return match