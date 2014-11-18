# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Proxy', fields ['hostname']
        db.delete_unique(u'proxylist_proxy', ['hostname'])

        # Adding unique constraint on 'Proxy', fields ['hostname', 'port']
        db.create_unique(u'proxylist_proxy', ['hostname', 'port'])


    def backwards(self, orm):
        # Removing unique constraint on 'Proxy', fields ['hostname', 'port']
        db.delete_unique(u'proxylist_proxy', ['hostname', 'port'])

        # Adding unique constraint on 'Proxy', fields ['hostname']
        db.create_unique(u'proxylist_proxy', ['hostname'])


    models = {
        u'proxylist.mirror': {
            'Meta': {'object_name': 'Mirror'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'output_type': ('django.db.models.fields.CharField', [], {'default': "'plm_v1'", 'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'proxylist.proxy': {
            'Meta': {'ordering': "('-last_check',)", 'unique_together': "(('hostname', 'port'),)", 'object_name': 'Proxy'},
            'anonymity_level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'elapsed_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'errors': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'next_check': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'port': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'proxy_type': ('django.db.models.fields.CharField', [], {'default': "'http'", 'max_length': '10'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'proxylist.proxycheckresult': {
            'Meta': {'object_name': 'ProxyCheckResult'},
            'check_end': ('django.db.models.fields.DateTimeField', [], {}),
            'check_start': ('django.db.models.fields.DateTimeField', [], {}),
            'forwarded': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_reveal': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mirror': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proxylist.Mirror']"}),
            'proxy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proxylist.Proxy']"}),
            'raw_response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'real_ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'response_end': ('django.db.models.fields.DateTimeField', [], {}),
            'response_start': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'proxylist.upload': {
            'Meta': {'object_name': 'Upload'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proxy_type': ('django.db.models.fields.CharField', [], {'default': "'http'", 'max_length': '10'})
        }
    }

    complete_apps = ['proxylist']