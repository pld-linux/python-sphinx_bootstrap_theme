#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx Bootstrap Theme - Python 2.x version
Summary(pl.UTF-8):	Motyw Bootstrap dla narzędzia Sphinx - wersja dla Pythona 2.x
Name:		python-sphinx_bootstrap_theme
Version:	0.8.1
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-bootstrap-theme/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-bootstrap-theme/sphinx-bootstrap-theme-%{version}.tar.gz
# Source0-md5:	705bb962d9ad21741f8b2efd6ebba2db
URL:		https://pypi.org/project/sphinx-bootstrap-theme/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-Sphinx >= 1.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Sphinx theme integrates the Bootstrap CSS/JavaScript framework
with various layout options, hierarchical menu navigation, and
mobile-friendly responsive design. It is configurable, extensible, and
can use any number of different Bootswatch CSS themes.

%description -l pl.UTF-8
Ten motyw Sphinksa integruje szkielet CSS/JavaScript Bootstrap z
różnymi opcjami układu, hierarchiczną nawigacją poprzez menu,
zaprojektowawany w sposób łatwo regujący, przyjazny dla urządzeń
przenośnych. Jest konfigurowalny, rozszerzalny, może używać dowolnej
liczby różnych motywów CSS Bootswatch.

%package -n python3-sphinx_bootstrap_theme
Summary:	Sphinx Bootstrap Theme - Python 3.x version
Summary(pl.UTF-8):	Motyw Bootstrap dla narzędzia Sphinx - wersja dla Pythona 3.x
Group:		Libraries/Python
Requires:	python3-Sphinx >= 1.6.1

%description -n python3-sphinx_bootstrap_theme
This Sphinx theme integrates the Bootstrap CSS/JavaScript framework
with various layout options, hierarchical menu navigation, and
mobile-friendly responsive design. It is configurable, extensible, and
can use any number of different Bootswatch CSS themes.

%description -n python3-sphinx_bootstrap_theme -l pl.UTF-8
Ten motyw Sphinksa integruje szkielet CSS/JavaScript Bootstrap z
różnymi opcjami układu, hierarchiczną nawigacją poprzez menu,
zaprojektowawany w sposób łatwo regujący, przyjazny dla urządzeń
przenośnych. Jest konfigurowalny, rozszerzalny, może używać dowolnej
liczby różnych motywów CSS Bootswatch.

%prep
%setup -q -n sphinx-bootstrap-theme-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE.txt README.rst TODO.rst
%{py_sitescriptdir}/sphinx_bootstrap_theme
%{py_sitescriptdir}/sphinx_bootstrap_theme-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_bootstrap_theme
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE.txt README.rst TODO.rst
%{py3_sitescriptdir}/sphinx_bootstrap_theme
%{py3_sitescriptdir}/sphinx_bootstrap_theme-%{version}-py*.egg-info
%endif
