import paypalrestsdk
import logging
from django.core.management.base import BaseCommand
from django.conf import settings
import json

PRODUCT = "product"
PLAN = "plan"

logger = logging.getLogger (__name__)

myapi = paypalrestsdk.configure({
  "mode": settings.PAYPAL_MODE, # sandbox or live
  "client_id": settings.PAYPAL_CLIENT_ID,
  "client_secret": settings.PAYPAL_CLIENT_SECRET
})

class Command(BaseCommand):
  
  help = """
  Manages Paypal Plans and Products
"""
  def add_arguments(self, parser):
    parser.add_argument(
        "--create",
        "-c",
        choices=[PRODUCT, PLAN],
        help="List Paypal products or plans"
    )
  
  def create_product(self):
       data = json.load(request.body)
       ret = myapi.get("v1/billing/plans")
       logger.debug(ret)

  def create_plan(self):
    pass

  def list_product(self):
    ret = myapi.get("v1/catalogs/products")
    logger.debug(ret)

  def list_plan(self):
    ret = myapi.get("v1/billing/plans")
    logger.debug(ret)

  def create(self, what):
    if what == PRODUCT:
       self.create_product()
    else:
        self.create_plan()
  
  def list(self, what):
    if what == PRODUCT:
       self.list_product()
    else:
       self.list_plan()

  def handle(slef, *args, **options):
    create_what = options.get("create")
