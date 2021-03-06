Summary:	Python interface to FAM (File Alternation Monitor)
Summary(pl.UTF-8):	Interfejs do FAM (File Alternation Monitor) dla Pythona
Name:		python-fam
Version:	1.1.1
Release:	4
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/python-fam/%{name}-%{version}.tar.gz
# Source0-md5:	f6c760c6d8e5ea69a3fce029f7973558
URL:		http://python-fam.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	fam-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python FAM provides a Python module to use the File Alteration Monitor
(http://oss.sgi.com/projects/fam/) in Python.

%description -l pl.UTF-8
Python FAM to moduł pozwalający korzystać z File Alternation Monitor
(monitora zmian plików). Więcej informacji o FAM dostępne jest na
stronie <http://oss.sgi.com/projects/fam/>.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install test*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_fam.so
%{_examplesdir}/%{name}-%{version}
