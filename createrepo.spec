Summary:	Creates a common metadata repository
Summary(pl.UTF-8):	Tworzenie wspólnego repozytorium metadanych
Name:		createrepo
Version:	0.4.10
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/metadata/generate/%{name}-%{version}.tar.gz
# Source0-md5:	733971b7aefd2597ad391feae01a6d15
Patch0:		%{name}-missingok.patch
URL:		http://linux.duke.edu/metadata/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python
Requires:	python-libxml2
Requires:	python-rpm
Requires:	yum-metadata-parser >= 1.1.1-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility will generate a common metadata repository from a
directory of RPM packages.

%description -l pl.UTF-8
To narzędzie tworzy wspólne repozytorium metadanych z katalogu
pakietów RPM.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
# note that these DO NEED executable bit set!
%attr(755,root,root) %{_datadir}/%{name}/genpkgmetadata.py
%attr(755,root,root) %{_datadir}/%{name}/dumpMetadata.py
%attr(755,root,root) %{_datadir}/%{name}/modifyrepo.py
%attr(755,root,root) %{_datadir}/%{name}/readMetadata.py
%{_mandir}/man8/createrepo.8*
