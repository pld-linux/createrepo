%include	/usr/lib/rpm/macros.python
Summary:	Creates a common metadata repository
Name:		createrepo
Version:	0.3.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/metadata/generate/%{name}-%{version}.tar.gz
URL:		http://linux.duke.edu/metadata/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
BuildRequires:  python-modules
BuildRequires:  python-devel
%pyrequires_eq  python
Requires:	python-libxml2
Requires:	python-rpm

%description
This utility will generate a common metadata repository from a
directory of rpm packages

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
