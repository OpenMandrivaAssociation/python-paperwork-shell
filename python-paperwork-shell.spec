%global module paperwork-shell

Summary:	Paperwork's shell interface
Name:		python-%{module}
Version:	2.2.0
Release:	1
Group:		Development/Python
License:	GPL-3.0-or-later
URL:		https://pypi.org/project/openpaperwork-shell/
Source0:	https://pypi.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Patch0:		python-paperwork-shell-2.2.0-fix_version_path.patch
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Paperwork's shell interface

Paperwork-shell provides 2 commands:

 *  paperwork-cli: Human-friendly command line interface. For instance,
    it can be useful if you want to use Paperwork through SSH.
 *  paperwork-json: Designed to be used in scripts. Results can be parsed
    in shell scripts using jq.

Both commands takes the same arguments as input. Only their outputs differ.

%files
%{_bindir}/paperwork-cli
%{_bindir}/paperwork-json
%{py_sitedir}/paperwork_shell
%{py_sitedir}/paperwork_shell-*.*-info

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n paperwork-shell-%{version}

%build
%py_build

%install
%py_install

