# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class WpCommentmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigIntegerField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpGalleryAlbums(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    album_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    album_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_gallery_albums'


class WpGalleryPics(models.Model):
    pic_id = models.AutoField(primary_key=True)
    album_id = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail_url = models.TextField()
    sorting_order = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    video = models.IntegerField()
    tags = models.TextField(blank=True, null=True)
    pic_name = models.TextField()
    album_cover = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_gallery_pics'


class WpGallerySettings(models.Model):
    setting_id = models.AutoField(primary_key=True)
    setting_key = models.CharField(max_length=100)
    setting_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_gallery_settings'


class WpLinks(models.Model):
    link_id = models.BigIntegerField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpOptions(models.Model):
    option_id = models.BigIntegerField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191, blank=True, null=True)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'


class WpPostmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


class WpPosts(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'wp_posts'


class WpTermRelationships(models.Model):
    object_id = models.BigIntegerField()
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigIntegerField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'


class WpTermmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    term_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_termmeta'


class WpTerms(models.Model):
    term_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_terms'


class WpUnTermmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    un_term_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_un_termmeta'


class WpUsermeta(models.Model):
    umeta_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class WpUsers(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'


class WpWppaAlbums(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    a_order = models.SmallIntegerField()
    main_photo = models.BigIntegerField()
    a_parent = models.BigIntegerField()
    p_order_by = models.SmallIntegerField()
    cover_linktype = models.TextField()
    cover_linkpage = models.BigIntegerField()
    owner = models.TextField()
    timestamp = models.TextField()
    modified = models.TextField()
    upload_limit = models.TextField()
    alt_thumbsize = models.TextField()
    default_tags = models.TextField()
    cover_type = models.TextField()
    suba_order_by = models.TextField()
    views = models.BigIntegerField()
    cats = models.TextField()
    scheduledtm = models.TextField()
    crypt = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wppa_albums'


class WpWppaComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    timestamp = models.TextField()
    photo = models.BigIntegerField()
    user = models.TextField()
    ip = models.TextField()
    email = models.TextField()
    comment = models.TextField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wppa_comments'


class WpWppaExif(models.Model):
    id = models.BigIntegerField(primary_key=True)
    photo = models.BigIntegerField()
    tag = models.TextField()
    description = models.TextField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wppa_exif'


class WpWppaIndex(models.Model):
    id = models.BigIntegerField(primary_key=True)
    slug = models.TextField()
    albums = models.TextField()
    photos = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wppa_index'


class WpWppaIptc(models.Model):
    id = models.BigIntegerField(primary_key=True)
    photo = models.BigIntegerField()
    tag = models.TextField()
    description = models.TextField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wppa_iptc'


class WpWppaPhotos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    album = models.BigIntegerField()
    ext = models.TextField()
    name = models.TextField()
    description = models.TextField()
    p_order = models.SmallIntegerField()
    mean_rating = models.TextField()
    linkurl = models.TextField()
    linktitle = models.TextField()
    linktarget = models.TextField()
    owner = models.TextField()
    timestamp = models.TextField()
    status = models.TextField()
    rating_count = models.BigIntegerField()
    tags = models.TextField()
    alt = models.TextField()
    filename = models.TextField()
    modified = models.TextField()
    location = models.TextField()
    views = models.BigIntegerField()
    page_id = models.BigIntegerField()
    exifdtm = models.TextField()
    videox = models.SmallIntegerField()
    videoy = models.SmallIntegerField()
    thumbx = models.SmallIntegerField()
    thumby = models.SmallIntegerField()
    photox = models.SmallIntegerField()
    photoy = models.SmallIntegerField()
    scheduledtm = models.TextField()
    custom = models.TextField()
    stereo = models.SmallIntegerField()
    crypt = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wppa_photos'


class WpWppaRating(models.Model):
    id = models.BigIntegerField(primary_key=True)
    timestamp = models.TextField()
    photo = models.BigIntegerField()
    value = models.SmallIntegerField()
    user = models.TextField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wppa_rating'


class WpWppaSession(models.Model):
    id = models.BigIntegerField(primary_key=True)
    session = models.TextField()
    timestamp = models.TextField()
    user = models.TextField()
    ip = models.TextField()
    status = models.TextField()
    data = models.TextField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wppa_session'
