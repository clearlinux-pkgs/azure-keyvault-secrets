#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-keyvault-secrets
Version  : 4.2.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/c8/05/9af6d7e61a50e99b4979f3adf76408f8908ef17b32524877daab9206889c/azure-keyvault-secrets-4.2.0.zip
Source0  : https://files.pythonhosted.org/packages/c8/05/9af6d7e61a50e99b4979f3adf76408f8908ef17b32524877daab9206889c/azure-keyvault-secrets-4.2.0.zip
Summary  : Microsoft Azure Key Vault Secrets Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-keyvault-secrets-python = %{version}-%{release}
Requires: azure-keyvault-secrets-python3 = %{version}-%{release}
Requires: azure-common~
Requires: azure-core
Requires: msrest
BuildRequires : azure-common~
BuildRequires : azure-core
BuildRequires : buildreq-distutils3
BuildRequires : msrest

%description
# Azure Key Vault Secret client library for Python
Azure Key Vault helps solve the following problems:

%package python
Summary: python components for the azure-keyvault-secrets package.
Group: Default
Requires: azure-keyvault-secrets-python3 = %{version}-%{release}

%description python
python components for the azure-keyvault-secrets package.


%package python3
Summary: python3 components for the azure-keyvault-secrets package.
Group: Default
Requires: python3-core
Provides: pypi(azure_keyvault_secrets)
Requires: pypi(azure_common)
Requires: pypi(azure_core)
Requires: pypi(msrest)

%description python3
python3 components for the azure-keyvault-secrets package.


%prep
%setup -q -n azure-keyvault-secrets-4.2.0
cd %{_builddir}/azure-keyvault-secrets-4.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608045361
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
