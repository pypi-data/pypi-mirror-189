ARG BASE_IMAGE="sandbox"
FROM ${BASE_IMAGE}

RUN pip install debugpy

ARG INSTALL_ZSH="true"
ARG UPGRADE_PACKAGES="true"
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
# COPY .devcontainer/library-scripts/*.sh /tmp/library-scripts/
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     # Remove imagemagick due to https://security-tracker.debian.org/tracker/CVE-2019-10131
#     && apt-get purge -y imagemagick imagemagick-6-common \
#     # Install common packages, non-root user
#     && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" \
#     # Clean up
#     && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

# Setup default python tools in a venv via pipx to avoid conflicts
ARG DEFAULT_UTILS="\
    pylint \
    flake8 \
    autopep8 \
    black \
    yapf \
    mypy \
    pydocstyle \
    pycodestyle \
    bandit \
    virtualenv"
ENV PIPX_HOME=/usr/local/py-utils
ENV PIPX_BIN_DIR=${PIPX_HOME}/bin
ENV PATH=${PATH}:${PIPX_BIN_DIR}
RUN mkdir -p ${PIPX_BIN_DIR} \
    && export PYTHONUSERBASE=/tmp/pip-tmp \
    && pip3 install --disable-pip-version-check --no-warn-script-location --no-cache-dir --user pipx \
    && /tmp/pip-tmp/bin/pipx install --pip-args=--no-cache-dir pipx \
    && echo "${DEFAULT_UTILS}" | xargs -n 1 /tmp/pip-tmp/bin/pipx install --system-site-packages --pip-args=--no-cache-dir --pip-args=--force-reinstall \
    && chown -R ${USER_UID}:${USER_GID} ${PIPX_HOME} \
    && rm -rf /tmp/pip-tmp
