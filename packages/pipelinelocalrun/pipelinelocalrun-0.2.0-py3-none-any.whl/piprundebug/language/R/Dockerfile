ARG BASE_IMAGE="ttt"
FROM ${BASE_IMAGE}

RUN apt-get update && apt-get -y install \
        python3-pip \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libxt-dev \
        libfontconfig1-dev \
        libcairo2-dev \
        && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U radian

RUN R -e "install.packages('languageserver', repos='https://packagemanager.rstudio.com/cran/__linux__/bionic/2020-06-04')"
RUN R -e 'install.packages("remotes"); remotes::install_github("ManuelHentschel/vscDebugger")'
RUN R -e 'remotes::install_version("Rcpp", "1.0.9", repos = "http://cran.us.r-project.org")'
# install httpgd???
# RUN R -e 'remotes::install_version("cpp11", "0.4.2", repos = "http://cran.us.r-project.org")'
# RUN R -e 'remotes::install_version("httpgd", "1.3.0", repos = "http://cran.us.r-project.org")'


RUN install2.r --error --skipinstalled --ncpus -1 \
        devtools \
        languageserver

RUN echo 'if (interactive() && Sys.getenv("TERM_PROGRAM") == "vscode") source(file.path(Sys.getenv("HOME"), ".vscode-R", "init.R"))' >>"${R_HOME}/etc/Rprofile.site"