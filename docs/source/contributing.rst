.. _contributing-to-carbonkivy:

Contributing to CarbonKivy
==========================

.. rst-class:: lead

    Thank you for considering contributing to CarbonKivy! We welcome contributions from everyone. By following these guidelines, you help us maintain a high standard of quality and ensure that your contributions are easy to review and integrate.

Table of Contents
-----------------

1. `Code of Conduct`_
2. `How to Contribute`_
3. `Reporting Bugs`_
4. `Requesting Features`_
5. `Coding Standards`_
6. `Support`_

Code of Conduct
---------------

Please read and follow our `Code of Conduct <https://github.com/CarbonKivy/CarbonKivy/blob/master/CODE_OF_CONDUCT.md>`_ to ensure a welcoming and inclusive environment for everyone.

How to Contribute
-----------------

1. **Fork the Repository**:
    - Click the "Fork" button at the top right of the CarbonKivy GitHub page.
    - Clone your forked repository to your local machine::

        git clone https://github.com/<your-username>/CarbonKivy.git
        cd CarbonKivy

2. **Install in Editable Mode**:
    - Set up the project in editable mode using pip::

        pip install -e .

3. **Create a Branch**:
    - Create a new branch for your changes::

        git checkout -b my-feature-branch

4. **Make Your Changes**:
    - Make your changes, ensuring proper type hinting and formatting your code using the Black formatter::

        pip install black
        black .

5. **Commit Your Changes**:
    - Commit your changes with a clear and descriptive commit message::

        git add .
        git commit -m "Add feature X to CarbonKivy"

6. **Push Your Branch**:
    - Push your branch to your forked repository::

        git push origin my-feature-branch

7. **Create a Pull Request**:
    - Go to the CarbonKivy GitHub page and click the "New Pull Request" button.
    - Provide a detailed description of your changes, including screenshots if applicable.

Reporting Bugs
--------------

Before reporting a bug, please:

1. **Search existing issues** on our GitHub Issues page to see if the bug has already been reported.
2. If the bug has not been reported, create a new issue using the **Bug Report** template. Provide a clear and descriptive title, a detailed description, and any relevant screenshots or code snippets.

Requesting Features
-------------------

To request a new feature:

1. **Search existing feature requests** on our GitHub Issues page to see if the feature has already been requested.
2. If the feature has not been requested, create a new issue using the **Feature Request** template. Provide a clear and descriptive title, a detailed description, and any relevant code or images.

Coding Standards
----------------

- **Type Hinting**: Ensure all functions and methods have proper type hints.
- **Formatting**: Use the Black formatter to format your code. You can install it using `pip install black` and format your code by running `black .` in the project directory.
- **Commit Messages**: Write clear and descriptive commit messages. Follow the Conventional Commits specification.

Support
-------

Join the CarbonKivy community to get support, share your projects, and collaborate with other developers. Here are some ways you can connect with us:

- **Discord**: Join our `CarbonKivy Community Server <https://discord.gg/jxZ5xr3pUt>`_.
- **Stack Overflow**: Feel free to reach out on `Stack Overflow <https://stackoverflow.com/tags/CarbonKivy>`_.
- **GitHub Discussions**: Participate in discussions and ask questions in the `GitHub Discussions <https://github.com/CarbonKivy/CarbonKivy/discussions>`_ section.
- **YouTube - CarbonKivy**: Follow us on YouTube `@CarbonKivy <https://youtube.com/@CarbonKivy>`_ for updates and announcements.

If you encounter any issues or have questions, feel free to reach out to the community or submit an issue on GitHub.

Thank you for your contributions and support!

Kartavya Shukla and Team - `CarbonKivy <https://github.com/CarbonKivy/CarbonKivy>`_

