# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminMenu(models.Model):
    parent_id = models.IntegerField()
    order = models.IntegerField()
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    uri = models.CharField(max_length=50, blank=True, null=True)
    permission = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_menu'


class AdminOperationLog(models.Model):
    user_id = models.IntegerField()
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    ip = models.CharField(max_length=255)
    input = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_operation_log'


class AdminPermissions(models.Model):
    name = models.CharField(unique=True, max_length=50)
    slug = models.CharField(max_length=50)
    http_method = models.CharField(max_length=255, blank=True, null=True)
    http_path = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_permissions'


class AdminRoleMenu(models.Model):
    role_id = models.IntegerField()
    menu_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_role_menu'


class AdminRolePermissions(models.Model):
    role_id = models.IntegerField()
    permission_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_role_permissions'


class AdminRoleUsers(models.Model):
    role_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_role_users'


class AdminRoles(models.Model):
    name = models.CharField(unique=True, max_length=50)
    slug = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_roles'


class AdminUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user_permissions'


class AdminUsers(models.Model):
    username = models.CharField(unique=True, max_length=190)
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_users'


class Categories(models.Model):
    parent_id = models.IntegerField()
    order = models.IntegerField()
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Sites(models.Model):
    category_id = models.IntegerField()
    title = models.CharField(max_length=50)
    thumb = models.CharField(max_length=200)
    describe = models.CharField(max_length=300)
    url = models.CharField(max_length=250)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sites'
