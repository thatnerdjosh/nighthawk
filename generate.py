from cookiecutter.main import cookiecutter

def get_context():
  context = {}

  context["generate_api"] = bool(
      input("Generate a Flask API (y/N): ").lower() == "y"
  )

  context["use_nuitka"] = bool(
      input("Compile the API with Nuitka (y/N): ").lower() == "y"
  )
  return context

ctx = get_context()
cookiecutter("scaffolds/simple-app", extra_context=ctx)
