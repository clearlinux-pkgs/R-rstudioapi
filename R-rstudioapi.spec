#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rstudioapi
Version  : 0.7
Release  : 42
URL      : https://cran.r-project.org/src/contrib/rstudioapi_0.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rstudioapi_0.7.tar.gz
Summary  : Safely Access the RStudio API
Group    : Development/Tools
License  : MIT
Requires: R-markdown
BuildRequires : R-markdown
BuildRequires : clr-R-helpers

%description
messages when it's not.

%prep
%setup -q -c -n rstudioapi

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504836676

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1504836676
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstudioapi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstudioapi
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rstudioapi
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rstudioapi/DESCRIPTION
/usr/lib64/R/library/rstudioapi/INDEX
/usr/lib64/R/library/rstudioapi/LICENSE
/usr/lib64/R/library/rstudioapi/Meta/Rd.rds
/usr/lib64/R/library/rstudioapi/Meta/features.rds
/usr/lib64/R/library/rstudioapi/Meta/hsearch.rds
/usr/lib64/R/library/rstudioapi/Meta/links.rds
/usr/lib64/R/library/rstudioapi/Meta/nsInfo.rds
/usr/lib64/R/library/rstudioapi/Meta/package.rds
/usr/lib64/R/library/rstudioapi/Meta/vignette.rds
/usr/lib64/R/library/rstudioapi/NAMESPACE
/usr/lib64/R/library/rstudioapi/NEWS.md
/usr/lib64/R/library/rstudioapi/R/rstudioapi
/usr/lib64/R/library/rstudioapi/R/rstudioapi.rdb
/usr/lib64/R/library/rstudioapi/R/rstudioapi.rdx
/usr/lib64/R/library/rstudioapi/doc/dialogs.R
/usr/lib64/R/library/rstudioapi/doc/dialogs.Rmd
/usr/lib64/R/library/rstudioapi/doc/dialogs.html
/usr/lib64/R/library/rstudioapi/doc/document-manipulation.R
/usr/lib64/R/library/rstudioapi/doc/document-manipulation.Rmd
/usr/lib64/R/library/rstudioapi/doc/document-manipulation.html
/usr/lib64/R/library/rstudioapi/doc/index.html
/usr/lib64/R/library/rstudioapi/doc/introduction.Rmd
/usr/lib64/R/library/rstudioapi/doc/introduction.html
/usr/lib64/R/library/rstudioapi/doc/projects.R
/usr/lib64/R/library/rstudioapi/doc/projects.Rmd
/usr/lib64/R/library/rstudioapi/doc/projects.html
/usr/lib64/R/library/rstudioapi/doc/r-session.R
/usr/lib64/R/library/rstudioapi/doc/r-session.Rmd
/usr/lib64/R/library/rstudioapi/doc/r-session.html
/usr/lib64/R/library/rstudioapi/doc/terminal.R
/usr/lib64/R/library/rstudioapi/doc/terminal.Rmd
/usr/lib64/R/library/rstudioapi/doc/terminal.html
/usr/lib64/R/library/rstudioapi/help/AnIndex
/usr/lib64/R/library/rstudioapi/help/aliases.rds
/usr/lib64/R/library/rstudioapi/help/paths.rds
/usr/lib64/R/library/rstudioapi/help/rstudioapi.rdb
/usr/lib64/R/library/rstudioapi/help/rstudioapi.rdx
/usr/lib64/R/library/rstudioapi/html/00Index.html
/usr/lib64/R/library/rstudioapi/html/R.css
