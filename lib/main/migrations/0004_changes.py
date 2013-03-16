# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.name'
        db.alter_column(u'main_user', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Inventory.name'
        db.alter_column(u'main_inventory', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Host.name'
        db.alter_column(u'main_host', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'LaunchJob.name'
        db.alter_column(u'main_launchjob', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'LaunchJob.job_type'
        db.alter_column(u'main_launchjob', 'job_type', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'Group.name'
        db.alter_column(u'main_group', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Credential.sudo_password'
        db.alter_column(u'main_credential', 'sudo_password', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Credential.name'
        db.alter_column(u'main_credential', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Credential.ssh_key_path'
        db.alter_column(u'main_credential', 'ssh_key_path', self.gf('django.db.models.fields.CharField')(max_length=4096))

        # Changing field 'Credential.ssh_password'
        db.alter_column(u'main_credential', 'ssh_password', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Credential.ssh_key_unlock'
        db.alter_column(u'main_credential', 'ssh_key_unlock', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'AuditTrail.resource_type'
        db.alter_column(u'main_audittrail', 'resource_type', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'AuditTrail.name'
        db.alter_column(u'main_audittrail', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Team.name'
        db.alter_column(u'main_team', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Project.local_repository'
        db.alter_column(u'main_project', 'local_repository', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Project.name'
        db.alter_column(u'main_project', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Project.scm_type'
        db.alter_column(u'main_project', 'scm_type', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'Project.default_playbook'
        db.alter_column(u'main_project', 'default_playbook', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Permission.job_type'
        db.alter_column(u'main_permission', 'job_type', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'Permission.name'
        db.alter_column(u'main_permission', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'LaunchJobStatus.name'
        db.alter_column(u'main_launchjobstatus', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'VariableData.name'
        db.alter_column(u'main_variabledata', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Organization.name'
        db.alter_column(u'main_organization', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Tag.name'
        db.alter_column(u'main_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

    def backwards(self, orm):

        # Changing field 'User.name'
        db.alter_column(u'main_user', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Inventory.name'
        db.alter_column(u'main_inventory', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Host.name'
        db.alter_column(u'main_host', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'LaunchJob.name'
        db.alter_column(u'main_launchjob', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'LaunchJob.job_type'
        db.alter_column(u'main_launchjob', 'job_type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Group.name'
        db.alter_column(u'main_group', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Credential.sudo_password'
        db.alter_column(u'main_credential', 'sudo_password', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Credential.name'
        db.alter_column(u'main_credential', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Credential.ssh_key_path'
        db.alter_column(u'main_credential', 'ssh_key_path', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Credential.ssh_password'
        db.alter_column(u'main_credential', 'ssh_password', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Credential.ssh_key_unlock'
        db.alter_column(u'main_credential', 'ssh_key_unlock', self.gf('django.db.models.fields.TextField')())

        # Changing field 'AuditTrail.resource_type'
        db.alter_column(u'main_audittrail', 'resource_type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'AuditTrail.name'
        db.alter_column(u'main_audittrail', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Team.name'
        db.alter_column(u'main_team', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Project.local_repository'
        db.alter_column(u'main_project', 'local_repository', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Project.name'
        db.alter_column(u'main_project', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Project.scm_type'
        db.alter_column(u'main_project', 'scm_type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Project.default_playbook'
        db.alter_column(u'main_project', 'default_playbook', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Permission.job_type'
        db.alter_column(u'main_permission', 'job_type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Permission.name'
        db.alter_column(u'main_permission', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'LaunchJobStatus.name'
        db.alter_column(u'main_launchjobstatus', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'VariableData.name'
        db.alter_column(u'main_variabledata', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Organization.name'
        db.alter_column(u'main_organization', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Tag.name'
        db.alter_column(u'main_tag', 'name', self.gf('django.db.models.fields.TextField')())

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.audittrail': {
            'Meta': {'object_name': 'AuditTrail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'audittrail_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'delta': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'resource_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Tag']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'audittrail_tags'", 'blank': 'True', 'to': "orm['main.Tag']"})
        },
        'main.credential': {
            'Meta': {'object_name': 'Credential'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'credential_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'credentials'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['main.Project']", 'blank': 'True', 'null': 'True'}),
            'ssh_key_data': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'ssh_key_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4096', 'blank': 'True'}),
            'ssh_key_unlock': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'ssh_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'sudo_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'credential_tags'", 'blank': 'True', 'to': "orm['main.Tag']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'credentials'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['main.Team']", 'blank': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'credentials'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['main.User']", 'blank': 'True', 'null': 'True'})
        },
        'main.group': {
            'Meta': {'object_name': 'Group'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'group_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hosts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'groups'", 'blank': 'True', 'to': "orm['main.Host']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['main.Inventory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'parents_rel_+'", 'blank': 'True', 'to': "orm['main.Group']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'group_tags'", 'blank': 'True', 'to': "orm['main.Tag']"})
        },
        'main.host': {
            'Meta': {'object_name': 'Host'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'host_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hosts'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['main.Inventory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'host_tags'", 'blank': 'True', 'to': "orm['main.Tag']"})
        },
        'main.inventory': {
            'Meta': {'object_name': 'Inventory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'inventory_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventories'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['main.Organization']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'inventory_tags'", 'blank': 'True', 'to': "orm['main.Tag']"})
        },
        'main.launchjob': {
            'Meta': {'object_name': 'LaunchJob'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'launchjob_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'credential': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'launch_jobs'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['main.Credential']", 'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'launch_jobs'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['main.Inventory']", 'blank': 'True', 'null': 'True'}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'launch_jobs'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['main.Project']", 'blank': 'True', 'null': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'launchjob_tags'", 'blank': 'True', 'to': "orm['main.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'launch_jobs'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': "orm['main.User']", 'blank': 'True', 'null': 'True'})
        },
        'main.launchjobstatus': {
            'Meta': {'object_name': 'LaunchJobStatus'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'launchjobstatus_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'launch_job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'launch_job_statuses'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['main.LaunchJob']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'result_data': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'launchjobstatus_tags'", 'blank': 'True', 'to': "orm['main.Tag']"})
        },
        'main.organization': {
            'Meta': {'object_name': 'Organization'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'admins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'admin_of_organizations'", 'blank': 'True', 'to': "orm['main.User']"}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'organization_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'organizations'", 'blank': 'True', 'to': "orm['main.Project']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'organization_tags'", 'blank': 'True', 'to': "orm['main.Tag']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'organizations'", 'blank': 'True', 'to': "orm['main.User']"})
        },
        'main.permission': {
            'Meta': {'object_name': 'Permission'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'permission_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'permissions'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['main.Project']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'permission_tags'", 'blank': 'True', 'to': "orm['main.Tag']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'permissions'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['main.Team']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'permissions'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['main.User']"})
        },
        'main.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'project_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'default_playbook': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': "orm['main.Inventory']"}),
            'local_repository': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'scm_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'project_tags'", 'blank': 'True', 'to': "orm['main.Tag']"})
        },
        'main.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'main.team': {
            'Meta': {'object_name': 'Team'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'team_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'organization': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'teams'", 'symmetrical': 'False', 'to': "orm['main.Organization']"}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'teams'", 'blank': 'True', 'to': "orm['main.Project']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'team_tags'", 'blank': 'True', 'to': "orm['main.Tag']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'teams'", 'blank': 'True', 'to': "orm['main.User']"})
        },
        'main.user': {
            'Meta': {'object_name': 'User'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'auth_user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'application_user'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_tags'", 'blank': 'True', 'to': "orm['main.Tag']"})
        },
        'main.variabledata': {
            'Meta': {'object_name': 'VariableData'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audit_trail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'variabledata_audit_trails'", 'blank': 'True', 'to': "orm['main.AuditTrail']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'data': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'variable_data'", 'null': 'True', 'blank': 'True', 'to': "orm['main.Group']"}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'variable_data'", 'null': 'True', 'blank': 'True', 'to': "orm['main.Host']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'variabledata_tags'", 'blank': 'True', 'to': "orm['main.Tag']"})
        }
    }

    complete_apps = ['main']