from setuptools import setup

BUILD_NUITKA = {{ cookiecutter.use_nuitka }}
def build_nuitka(build_func):
  """
  Custom build function to trigger Nuitka compilation (if chosen).
  """
  if not BUILD_NUITKA:
      return

  build_func.run_command('build_nuitka', {'build_dir': 'build', 'output_path': {{ cookiecutter.project_name }} })

setup(
  name="{{ cookiecutter.project_name }}",
  version="0.1.0",
  cmdclass={'build': build_nuitka} if BUILD_NUITKA else {},

  # Define Nuitka specific build options (optional)
  build_nuitka = {
      'build_dir': 'build',
      'output_path': output_exe,
  }
)
