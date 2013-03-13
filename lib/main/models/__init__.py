from django.db import models
from django.db.models import CASCADE, SET_NULL, PROTECT

# TODO: jobs and events model TBD
# TODO: reporting model TBD

class CommonModel(models.Model):
    ''' 
    common model for all object types that have these standard fields 
    '''

    class Meta:
        abstract = True

    name          = models.TextField()
    description   = models.TextField()
    creation_date = models.DateField()
    tags          = models.ManyToManyField('Tag', related_name='%(class)s_tags') 
    audit_trail   = models.ManyToManyField('AuditTrail', related_name='%(class)s_audit_trails')
    active        = models.BooleanField(default=True)
 
class Tag(models.Model):
    ''' 
    any type of object can be given a search tag 
    '''
    
    class Meta:
        app_label = 'main'

    name = models.TextField()
 
 
class AuditTrail(CommonModel):
    ''' 
    changing any object records the change 
    '''
    
    class Meta:
        app_label = 'main'
 
    resource_type = models.TextField()
    modified_by   = models.ForeignKey('User', on_delete=SET_NULL, null=True)
    delta         = models.TextField() # FIXME: switch to JSONField
    detail        = models.TextField()
    comment       = models.TextField()
    tag           = models.ForeignKey('Tag', on_delete=SET_NULL, null=True)

class Organization(CommonModel):
    ''' 
    organizations are the basic unit of multi-tenancy divisions 
    '''    
    
    class Meta:
        app_label = 'main'

    users    = models.ManyToManyField('User', related_name='organizations')
    admins   = models.ManyToManyField('User', related_name='admin_of_organizations')
    projects = models.ManyToManyField('Project', related_name='organizations')

class Inventory(CommonModel):
    ''' 
    an inventory source contains lists and hosts.
    '''
    
    class Meta:
        app_label = 'main'
  
    organization = models.ForeignKey(Organization, null=True, on_delete=SET_NULL, related_name='inventories')    

class Host(CommonModel):
    '''
    A managed node
    '''
    
    class Meta:
        app_label = 'main'

    inventory = models.ForeignKey('Inventory', null=True, on_delete=SET_NULL, related_name='hosts')
    

class Group(CommonModel):
    '''
    A group of managed nodes.  May belong to multiple groups
    '''
    
    class Meta:
        app_label = 'main'

    inventory = models.ForeignKey('Inventory', null=True, on_delete=SET_NULL, related_name='groups')
    parents   = models.ManyToManyField('self', related_name='children') 

# FIXME: audit nullables
# FIXME: audit cascades

class VariableData(CommonModel):
    '''
    A set of host or group variables
    '''  
    
    class Meta:
        app_label = 'main'

    host  = models.ForeignKey('Host', null=True, default=None, blank=True, on_delete=CASCADE, related_name='variable_data')
    group = models.ForeignKey('Group', null=True, default=None, blank=True, on_delete=CASCADE, related_name='variable_data')
    data  = models.TextField() # FIXME: JsonField

class User(CommonModel):
    '''
    Basic user class
    '''
    
    class Meta:
        app_label = 'main'

    # FIXME: how to integrate with Django auth?

    auth_user     = models.OneToOneField('auth.User', related_name='application_user')

class Credential(CommonModel):
    '''
    A credential contains information about how to talk to a remote set of hosts
    Usually this is a SSH key location, and possibly an unlock password.
    If used with sudo, a sudo password should be set if required.
    '''
    
    class Meta:
        app_label = 'main'

    user            = models.ForeignKey('User', null=True, default=None, blank=True, on_delete=SET_NULL, related_name='credentials')
    project         = models.ForeignKey('Project', null=True, default=None, blank=True, on_delete=SET_NULL, related_name='credentials')
    team            = models.ForeignKey('Team', null=True, default=None, blank=True, on_delete=SET_NULL, related_name='credentials')

    ssh_key_path    = models.TextField(blank=True, default='')
    ssh_key_data    = models.TextField(blank=True, default='') # later
    ssh_key_unlock  = models.TextField(blank=True, default='')
    ssh_password    = models.TextField(blank=True, default='')
    sudo_password   = models.TextField(blank=True, default='')
    

class Team(CommonModel):
    '''
    A team is a group of users that work on common projects.
    '''
    
    class Meta:
        app_label = 'main'
    
    projects        = models.ManyToManyField('Project', related_name='teams')
    users           = models.ManyToManyField('User', related_name='teams')
    organization    = models.ManyToManyField('Organization', related_name='teams')

class Project(CommonModel):
    '''  
    A project represents a playbook git repo that can access a set of inventories
    '''   
    
    class Meta:
        app_label = 'main'
 
    inventories      = models.ManyToManyField('Inventory', related_name='projects')
    local_repository = models.TextField()
    scm_type         = models.TextField()
    default_playbook = models.TextField()

class Permission(CommonModel):
    '''
    A permission allows a user, project, or team to be able to use an inventory source.
    '''
    
    class Meta:
        app_label = 'main'

    user            = models.ForeignKey('User', null=True, on_delete=SET_NULL, related_name='permissions')
    project         = models.ForeignKey('Project', null=True, on_delete=SET_NULL, related_name='permissions')
    team            = models.ForeignKey('Team', null=True, on_delete=SET_NULL, related_name='permissions')
    job_type        = models.TextField()

# TODO: other job types (later)

class LaunchJob(CommonModel):
    ''' 
    a launch job is a request to apply a project to an inventory source with a given credential 
    '''
    
    class Meta:
        app_label = 'main'

    inventory      = models.ForeignKey('Inventory', on_delete=SET_NULL, null=True, default=None, blank=True, related_name='launch_jobs')
    credential     = models.ForeignKey('Credential', on_delete=SET_NULL, null=True, default=None, blank=True, related_name='launch_jobs')
    project        = models.ForeignKey('Project', on_delete=SET_NULL, null=True, default=None, blank=True, related_name='launch_jobs')
    user           = models.ForeignKey('User', on_delete=SET_NULL, null=True, default=None, blank=True, related_name='launch_jobs')
    job_type       = models.TextField()
    
 

# TODO: Events

class LaunchJobStatus(CommonModel):
    
    class Meta:
        app_label = 'main'

    launch_job     = models.ForeignKey('LaunchJob', null=True, on_delete=SET_NULL, related_name='launch_job_statuses')
    status         = models.IntegerField()
    result_data    = models.TextField()
     

# TODO: reporting (MPD)


