Summary:	Creates a common metadata repository
Summary(pl):	Tworzenie wspólnego repozytorium metadanych
Name:		createrepo
Version:	0.4.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/metadata/generate/%{name}-%{version}.tar.gz
# Source0-md5:	b1f07dd576cf604e28173d4a18897468
# Source0-size:	20480
URL:		http://linux.duke.edu/metadata/
BuildRequires:  python-devel
BuildRequires:  python-modules
%pyrequires_eq  python
Requires:	python-libxml2
Requires:	python-rpm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility will generate a common metadata repository from a
directory of RPM packages.

%description -l pl
To narzêdzie tworzy wspólne repozytorium metadanych z katalogu
pakietów RPM.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
