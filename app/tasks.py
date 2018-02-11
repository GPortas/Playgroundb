from invoke import task

MANAGE_PATH = "manage.py"

@task
def installrequirements(ctx):
    ctx.run("pip3 install -r requirements.txt")

@task
def testall(ctx):
    testunit(ctx)
    testintegration(ctx)

@task
def testunit(ctx):
    build(ctx, 'api-test')
    print('Executing unit tests...')
    ctx.run("export PYTHONPATH='.';python3 " + MANAGE_PATH + " tests unit")

@task
def testoneunit(ctx, test_case):
    build(ctx, 'api-test')
    print('Executing unit test...')
    ctx.run("export PYTHONPATH='.';python3 " + MANAGE_PATH + " tests unit " + test_case)

@task
def testintegration(ctx):
    setupintegration(ctx)
    ctx.run("export PYTHONPATH='.';python3 " + MANAGE_PATH + " tests integration")

@task
def testoneintegration(ctx, test_case):
    setupintegration(ctx)
    ctx.run("export PYTHONPATH='.';python3 " + MANAGE_PATH + " tests integration " + test_case)

@task
def testfunctional(ctx):
    build(ctx, "api-development")
    print('Executing functional tests...')
    ctx.run("export PYTHONPATH='.';python3 " + MANAGE_PATH + " tests functional")

@task
def testonefunctional(ctx, test_case):
    build(ctx, "api-development")
    print('Executing functional tests...')
    ctx.run("export PYTHONPATH='.';python3 " + MANAGE_PATH + " tests functional " + test_case)

def setupintegration(ctx):
    build(ctx, "api-test")
    print('Executing integration tests...')

@task
def build(ctx, env):
    checkenvironment(env)
    print("Building environment %s..." % env)
    ctx.run("sed 's/%ENVIRONMENT%/" + env + "/g' ./app/configuration/template/settings.template.py > ./app/configuration/settings.py")

def checkenvironment(env):
    if env != 'api-development' and env != 'api-production' and env != 'api-test':
        raise ValueError("Invalid environment %s" % env)

