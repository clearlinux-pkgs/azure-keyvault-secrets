#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-keyvault-secrets
Version  : 4.1.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/0e/a1/02fd621bf5f23463d23d9e8d563f85137cac6d07bccdea43e0474c938c44/azure-keyvault-secrets-4.1.0.zip
Source0  : https://files.pythonhosted.org/packages/0e/a1/02fd621bf5f23463d23d9e8d563f85137cac6d07bccdea43e0474c938c44/azure-keyvault-secrets-4.1.0.zip
Summary  : Microsoft Azure Key Vault Secrets Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-keyvault-secrets-python = %{version}-%{release}
Requires: azure-keyvault-secrets-python3 = %{version}-%{release}
Requires: azure-core
Requires: msrest
BuildRequires : azure-core
BuildRequires : buildreq-distutils3
BuildRequires : msrest

%description
# Azure Key Vault Secret client library for Python
Azure Key Vault helps solve the following problems:
- Secrets management (this library) -
securely store and control access to tokens, passwords, certificates, API keys,
and other secrets
- Cryptographic key management
([azure-keyvault-keys](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets)) -
create, store, and control access to the keys used to encrypt your data
- Certificate management
([azure-keyvault-certificates](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-certificates)) -
create, manage, and deploy public and private SSL/TLS certificates

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
Requires: pypi(azure_core)
Requires: pypi(msrest)

%description python3
python3 components for the azure-keyvault-secrets package.


%prep
%setup -q -n azure-keyvault-secrets-4.1.0
cd %{_builddir}/azure-keyvault-secrets-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591206986
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
