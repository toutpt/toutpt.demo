import logging
from Products.CMFCore.utils import getToolByName
from plone.app.controlpanel.security import ISecuritySchema

POLICY = 'toutpt.demo'
PROFILE = 'profile-%s:default' % POLICY


def quickinstall_addons(context, install=None, uninstall=None, upgrades=None):
    logger = logging.getLogger(PROFILE)
    qi = getToolByName(context, 'portal_quickinstaller')

    if install is not None:
        for addon in install:
            if qi.isProductInstallable(addon):
                qi.installProduct(addon)
            else:
                logger.error('%s can t be installed' % addon)

    if uninstall is not None:
        qi.uninstallProducts(uninstall)

    if upgrades is not None:
        if upgrades in ("all", True):
            #TODO: find which addons should be upgrades
            installedProducts = qi.listInstalledProducts(showHidden=True)
            upgrades = [p['id'] for p in installedProducts]
        for upgrade in upgrades:
            # do not try to upgrade myself -> recursion
            if upgrade == POLICY:
                continue
            try:
                qi.upgradeProduct(upgrade)
            except KeyError:
                logger.error('can t upgrade %s' % upgrade)

def common(context):
    logger = logging.getLogger(PROFILE)

    portal_migration = getToolByName(context, 'portal_migration')
    portal_migration.upgrade()
    logger.info("Ran Plone Upgrade")

    #upgrades installed addons
    quickinstall_addons(context, upgrades=True)

    context.runAllImportStepsFromProfile(PROFILE)
    logger.info("Apply %s" % PROFILE)
