Summary:	Python interface to FAM (File Alternation Monitor)
Summary(pl):	Interfejs do FAM (File Alternation Monitor) dla Pythona
Name:		python-fam
Version:	1.1.1
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/python-fam/%{name}-%{version}.tar.gz
# Source0-md5:	f6c760c6d8e5ea69a3fce029f7973558
URL:		http://python-fam.sourceforge.net/
BuildRequires:	perl-base
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python FAM provides a Python module to use the File Alteration Monitor
(http://oss.sgi.com/projects/fam/) in Python.

%description -l pl
Python FAM to modu³ pozwalaj±cy korzystaæ z File Alternation Monitor
(monitora zmian plików). Wiêcej informacji o FAM dostêpne jest na
stronie <http://oss.sgi.com/projects/fam/>.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install test*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_fam.so
%{_examplesdir}/%{name}-%{version}
