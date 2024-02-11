# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-stevedore
Epoch: 100
Version: 5.1.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Manage dynamic plugins for Python applications
License: Apache-2.0
URL: https://github.com/openstack/stevedore/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
("plugins") at runtime. Many applications implement their own library
for doing this, using **import** or importlib. stevedore avoids creating
yet another extension mechanism by building on top of setuptools entry
points. The code for managing entry points tends to be repetitive,
though, so stevedore provides manager classes for implementing common
patterns for using dynamically loaded extensions.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-stevedore
Summary: Manage dynamic plugins for Python applications
Requires: python3
Provides: python3-stevedore = %{epoch}:%{version}-%{release}
Provides: python3dist(stevedore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-stevedore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(stevedore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-stevedore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(stevedore) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-stevedore
Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
("plugins") at runtime. Many applications implement their own library
for doing this, using **import** or importlib. stevedore avoids creating
yet another extension mechanism by building on top of setuptools entry
points. The code for managing entry points tends to be repetitive,
though, so stevedore provides manager classes for implementing common
patterns for using dynamically loaded extensions.

%files -n python%{python3_version_nodots}-stevedore
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-stevedore
Summary: Manage dynamic plugins for Python applications
Requires: python3
Provides: python3-stevedore = %{epoch}:%{version}-%{release}
Provides: python3dist(stevedore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-stevedore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(stevedore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-stevedore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(stevedore) = %{epoch}:%{version}-%{release}

%description -n python3-stevedore
Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
("plugins") at runtime. Many applications implement their own library
for doing this, using **import** or importlib. stevedore avoids creating
yet another extension mechanism by building on top of setuptools entry
points. The code for managing entry points tends to be repetitive,
though, so stevedore provides manager classes for implementing common
patterns for using dynamically loaded extensions.

%files -n python3-stevedore
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-stevedore
Summary: Manage dynamic plugins for Python applications
Requires: python3
Provides: python3-stevedore = %{epoch}:%{version}-%{release}
Provides: python3dist(stevedore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-stevedore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(stevedore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-stevedore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(stevedore) = %{epoch}:%{version}-%{release}

%description -n python3-stevedore
Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
("plugins") at runtime. Many applications implement their own library
for doing this, using **import** or importlib. stevedore avoids creating
yet another extension mechanism by building on top of setuptools entry
points. The code for managing entry points tends to be repetitive,
though, so stevedore provides manager classes for implementing common
patterns for using dynamically loaded extensions.

%files -n python3-stevedore
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
