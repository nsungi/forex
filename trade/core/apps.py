from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    
    
    
# permission level
"""
    def ready(self):
        from django.contrib.auth.models import Permission

        # Create a permission for customer accounts
        customer_permission = Permission.objects.get_or_create(
            codename='customer_permission',
            name='Customer Permission',
            content_type__app_label=self.label,
        )

        # Create a permission for admin accounts
        admin_permission = Permission.objects.get_or_create(
            codename='admin_permission',
            name='Admin Permission',
            content_type__app_label=self.label,
        )
"""         
         
#other implementation

"""
        
       
from django.apps import AppConfig
from django.contrib.auth.models import Permission

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        # Check for any custom permission creation causing the issue
        customer_permission = Permission.objects.get_or_create(
            codename='custom_permission',
            name='Custom Permission',
            content_type_id=???  # Make sure to replace with the appropriate content_type_id
        )
"""
        
                