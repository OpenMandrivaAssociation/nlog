%define name nlog
%define version 1.0
%define release %mkrel 3

Summary: Logging library for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/nlog/%{name}-%{version}-src.zip
Source1: nlog.pc
#gw I don't know how else I can make nant build it the right way
Patch: nlog-1.0-fix-build.patch
License: BSD
Group: System/Libraries
Url:  http://www.nlog-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: nant
BuildRequires: dos2unix
BuildArch: noarch

%description
This is a .NET Library for logging.

%prep
%setup -q -n NLog-%version
%patch -p1
dos2unix *.txt

%build
nant

%install
rm -rf %{buildroot}
cd build/mono-2.0-debug/bin/
gacutil -i NLog.dll -root %buildroot%_prefix/lib/
gacutil -i Policy.1.0.NLog.dll -root %buildroot%_prefix/lib/
mkdir -p %buildroot%_prefix/lib/mono/%name
cd %buildroot%_prefix/lib/mono/%name
ln -s ../gac/*/*/*.dll .
mkdir -p %buildroot%_prefix/lib/pkgconfig
cp %SOURCE1 %buildroot%_prefix/lib/pkgconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%_prefix/lib/mono/gac/NLog/
%_prefix/lib/mono/gac/Policy.1.0.NLog/
%_prefix/lib/mono/%name

%package devel
Summary: Development files for %{name}
Group: Development/mono
Requires: %{name} = %{version}-%{release}

%description devel
Development files for %{name}

%files devel
%defattr(-,root,root)
%_prefix/lib/pkgconfig/nlog.pc

