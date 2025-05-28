.. _build-instructions:

Build Intructions
=================

.. rst-class:: lead

	This page covers all information you need to know before compiling your softwares for different platforms like Android, iOS, Linux, macOS and Windows.

Android and iOS
---------------

.. figure:: /_static/images/build_ins/androidios.svg
	:class: centered

- Use `buildozer <https://github.com/kivy/buildozer>`_ to compile your app to an APK or Android App Bundle for Android, or an IPA for iOS.

- Add :confval:`carbonkivy` or the github url :confval:`https://github.com/CarbonKivy/CarbonKivy/archive/master.zip` for development verion, to the requirements list.

	.. code-block:: spec

		requirements = python3, kivy==2.3.0, carbonkivy

		# requirements = python3, kivy==2.3.0, https://github.com/CarbonKivy/CarbonKivy/archive/master.zip # development version

.. caution::

	You need to remove pre-compiled carbonkivy library if you are rebuilding with buildozer and also updated the version to be used. Prefered to use :confval:`buildozer android clean`.

Generate Android Build Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can generate Android Build worlflows and Jupyer Notebooks for both **Github Actions** and **Google Colab** using the `KvDeveloper CLI <https://gtihub.com/Novfensec/KvDeveloper>`_ .

In case of Google Colab you have the priviledge to import you app folder from your personal drive.

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

