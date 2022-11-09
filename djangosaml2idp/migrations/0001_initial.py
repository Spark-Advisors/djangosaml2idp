# Generated by Django 2.2.9 on 2020-02-05 21:13

import djangosaml2idp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ServiceProvider",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dt_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "dt_updated",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated at"
                    ),
                ),
                (
                    "entity_id",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Entity ID"
                    ),
                ),
                (
                    "pretty_name",
                    models.CharField(
                        blank=True,
                        help_text="For display purposes, can be empty",
                        max_length=255,
                        verbose_name="Pretty Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "metadata_expiration_dt",
                    models.DateTimeField(verbose_name="Metadata valid until"),
                ),
                (
                    "remote_metadata_url",
                    models.CharField(
                        blank=True,
                        help_text="If set, metadata will be fetched upon saving into the local metadata xml field, and automatically be refreshed after the expiration timestamp.",
                        max_length=512,
                        verbose_name="Remote metadata URL",
                    ),
                ),
                (
                    "local_metadata",
                    models.TextField(
                        blank=True,
                        help_text="XML containing the metadata",
                        verbose_name="Local Metadata XML",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "_processor",
                    models.CharField(
                        default=djangosaml2idp.models.get_default_processor,
                        help_text="Import string for the (access) Processor to use.",
                        max_length=256,
                        verbose_name="Processor",
                    ),
                ),
                (
                    "_attribute_mapping",
                    models.TextField(
                        default=djangosaml2idp.models.get_default_attribute_mapping,
                        help_text="dict with the mapping from django attributes to saml attributes in the identity.",
                        verbose_name="Attribute mapping",
                    ),
                ),
                (
                    "_nameid_field",
                    models.CharField(
                        blank=True,
                        help_text="Attribute on the user to use as identifier during the NameID construction. Can be a callable. If not set, this will default to settings.SAML_IDP_DJANGO_USERNAME_FIELD; if that is not set, it will use the `USERNAME_FIELD` attribute on the active user model.",
                        max_length=64,
                        verbose_name="NameID Field",
                    ),
                ),
                (
                    "_sign_response",
                    models.BooleanField(
                        blank=True,
                        help_text='If not set, default to the "sign_response" setting of the IDP. If that one is not set, default to False.',
                        null=True,
                        verbose_name="Sign response",
                    ),
                ),
                (
                    "_sign_assertion",
                    models.BooleanField(
                        blank=True,
                        help_text='If not set, default to the "sign_assertion" setting of the IDP. If that one is not set, default to False.',
                        null=True,
                        verbose_name="Sign assertion",
                    ),
                ),
                (
                    "_signing_algorithm",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
                                "SIG_RSA_SHA1",
                            ),
                            (
                                "http://www.w3.org/2001/04/xmldsig-more#rsa-sha224",
                                "SIG_RSA_SHA224",
                            ),
                            (
                                "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
                                "SIG_RSA_SHA256",
                            ),
                            (
                                "http://www.w3.org/2001/04/xmldsig-more#rsa-sha384",
                                "SIG_RSA_SHA384",
                            ),
                            (
                                "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512",
                                "SIG_RSA_SHA512",
                            ),
                        ],
                        help_text="If not set, use settings.SAML_AUTHN_SIGN_ALG.",
                        max_length=256,
                        null=True,
                        verbose_name="Signing algorithm",
                    ),
                ),
                (
                    "_digest_algorithm",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("http://www.w3.org/2000/09/xmldsig#sha1", "DIGEST_SHA1"),
                            (
                                "http://www.w3.org/2001/04/xmldsig-more#sha224",
                                "DIGEST_SHA224",
                            ),
                            (
                                "http://www.w3.org/2001/04/xmlenc#sha256",
                                "DIGEST_SHA256",
                            ),
                            (
                                "http://www.w3.org/2001/04/xmldsig-more#sha384",
                                "DIGEST_SHA384",
                            ),
                            (
                                "http://www.w3.org/2001/04/xmlenc#sha512",
                                "DIGEST_SHA512",
                            ),
                            (
                                "http://www.w3.org/2001/04/xmlenc#ripemd160",
                                "DIGEST_RIPEMD160",
                            ),
                        ],
                        help_text="If not set, default to settings.SAML_AUTHN_DIGEST_ALG.",
                        max_length=256,
                        null=True,
                        verbose_name="Digest algorithm",
                    ),
                ),
                (
                    "_encrypt_saml_responses",
                    models.BooleanField(
                        help_text="If not set, default to settings.SAML_ENCRYPT_AUTHN_RESPONSE. If that one is not set, default to False.",
                        null=True,
                        verbose_name="Encrypt SAML Response",
                    ),
                ),
            ],
            options={
                "verbose_name": "Service Provider",
                "verbose_name_plural": "Service Providers",
            },
        ),
        migrations.AddIndex(
            model_name="serviceprovider",
            index=models.Index(
                fields=["entity_id"], name="djangosaml2_entity__5fb9e3_idx"
            ),
        ),
    ]
