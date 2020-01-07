#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-pcre
Version  : 0.7
Release  : 6
URL      : https://files.pythonhosted.org/packages/9d/af/61435bd163f01fe3709fca9b1f79e4978d8089ee671d2e004fc85e10de29/python-pcre-0.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/af/61435bd163f01fe3709fca9b1f79e4978d8089ee671d2e004fc85e10de29/python-pcre-0.7.tar.gz
Summary  : Python PCRE bindings
Group    : Development/Tools
License  : BSD-3-Clause
Requires: python-pcre-license = %{version}-%{release}
Requires: python-pcre-python = %{version}-%{release}
Requires: python-pcre-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pcre-dev

%description
python-pcre
===========
Python bindings for PCRE regex engine.
Requirements
------------

%package license
Summary: license components for the python-pcre package.
Group: Default

%description license
license components for the python-pcre package.


%package python
Summary: python components for the python-pcre package.
Group: Default
Requires: python-pcre-python3 = %{version}-%{release}

%description python
python components for the python-pcre package.


%package python3
Summary: python3 components for the python-pcre package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-pcre package.


%prep
%setup -q -n python-pcre-0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550437780
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-pcre
cp LICENSE %{buildroot}/usr/share/package-licenses/python-pcre/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-pcre/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
