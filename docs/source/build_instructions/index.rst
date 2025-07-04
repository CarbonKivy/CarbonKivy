.. _build-instructions:

Build Instructions
==================

.. rst-class:: lead

    This page covers all information you need to know before compiling your softwares for different platforms like Android, iOS, Linux, macOS and Windows.

Android and iOS
---------------

.. figure:: /_static/images/build_ins/androidios.svg
    :class: centered

- Use `buildozer <https://github.com/kivy/buildozer>`_ to compile your app to an APK or Android App Bundle for Android, or an IPA for iOS.

- Add :confval:`carbonkivy` or the github url :confval:`https://github.com/CarbonKivy/CarbonKivy/archive/master.zip` for development verion, to the requirements list.

    .. code-block:: spec

        requirements = python3, kivy==2.3.0, android, carbonkivy

        # requirements = python3, kivy==2.3.0, android, https://github.com/CarbonKivy/CarbonKivy/archive/master.zip # development version

.. caution::

    You need to remove pre-compiled carbonkivy library if you are rebuilding with buildozer and also updated the version to be used. Prefered to use :confval:`buildozer android clean`.

Generate Android Build Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can generate Android Build worlflows and Jupyer Notebooks for both **Github Actions** and **Google Colab** using the `KvDeveloper CLI <https://gtihub.com/Novfensec/KvDeveloper>`_ .

In case of Google Colab you have the priviledge to import your app folder from your personal drive.

Build debug apks and unsigned release apks and aabs.

- To generate a github based workflow run below command in the root directory of your app.

    .. code-block:: bash

        kvdeveloper config-build-setup android --external github

- To generate a colab base jupyter notebook run below command in the root directory of your app.

    .. code-block:: bash

        kvdeveloper config-build-setup android --external colab

Compiling to iOS using `kivy-ios toolchain <https://github.com/kivy/kivy-ios>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    toolchain build python3 kivy
    toolchain pip install --no-deps carbonkivy
    # toolchain pip install --no-deps gticlonedir/carbonkivy # clone development version from github and specify the path

Desktop - Linux, macOS and Windows
----------------------------------

Using `Pyinstaller <https://github.com/pyinstaller/pyinstaller>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need to just inlcude our data assets (.kv, .ttf, .png etc.) and rest all will be managed by pyinstaller.

Sample :class:`spec` file is given below. Make additions for your own data files with the pattern for them to be present in the final distribution.

Example if you want to inlcude all your kv files under the :class:`root` directory and assets under :class:`assets/` directory, the inclusion can be done like below:

    .. code-block:: spec

        import os, glob
        from pathlib import Path

        base_dir = Path(__file__).parent

        data_files = []

        for files in glob.glob(os.path.join(base_dir, "**", "*.{png, jpg, ttf, kv}"), recursive=True):

            data_files.append((Path(files), Path(os.path.dirname(files)).relative_to(base_dir)))

        ...

        exe = EXE(
            ...

            data_files,

            ...
        )

        ...

:class:`main.spec`
^^^^^^^^^^^^^^^^^^

For compilation run below command:

    .. code-block:: bash

        pyinstaller -y main.spec

.. code-block:: spec

    # -*- mode: python ; coding: utf-8 -*-
    import os, glob
    from pathlib import Path
    from kivy_deps import sdl2, glew
    from pathlib import Path

    from carbonkivy.config import ROOT

    data = []

    for files in glob.glob(os.path.join(ROOT, "**", "*.{ttf, kv}"), recursive=True):

        data.append((Path(files), Path(os.path.dirname(files)).relative_to(Path(ROOT).parent)))

    a = Analysis(
        ['main.py'],
        pathex=[],
        binaries=[],
        datas=data,
        hiddenimports=["carbonkivy"],
        hookspath=[],
        hooksconfig={},
        runtime_hooks=[],
        excludes=[],
        noarchive=False,
        optimize=0,
    )
    pyz = PYZ(a.pure)

    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.datas,
        *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
        name='main',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
    )