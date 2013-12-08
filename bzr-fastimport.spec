Summary:	Bzr plugin for fast loading of data from other VCS tools
Name:		bzr-fastimport
Version:	0.13.0
Release:	2
Group:		Development/Languages
# Some modules in the exporters/ subdir are MIT-licensed.
License:	GPL v2+ and MIT
Source0:	http://launchpad.net/bzr-fastimport/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	e47115774d44ae0c3b027ae0374aa52e
URL:		https://launchpad.net/bzr-fastimport
Patch0:		bug-1101776.patch
Patch1:		bug-541626.patch
BuildRequires:	bzr
BuildRequires:	python-distribute
Requires:	bzr
Requires:	python-fastimport
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bazaar Fast Import is a plugin providing fast loading of revision
control data into Bazaar. It is designed to be used in combination
with front-end programs that generate a command/data stream for it to
process. Front-ends are available for a wide range of foreign VCS
tools including Subversion, CVS, Git, Mercurial, Darcs and Perforce.
New front-ends are easy to develop in whatever programming language
you prefer, making Bazaar Fast Import useful for teams needing a
custom migration solution.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	-O2 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%py_postclean

# not interested to package tests at runtime
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/bzrlib/plugins/fastimport/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.txt
%{py_sitescriptdir}/bzr_fastimport-*.egg-info

%dir %{py_sitescriptdir}/bzrlib
%dir %{py_sitescriptdir}/bzrlib/plugins

%dir %{py_sitescriptdir}/bzrlib/plugins/fastimport
%{py_sitescriptdir}/bzrlib/plugins/fastimport/*.py[co]
%dir %{py_sitescriptdir}/bzrlib/plugins/fastimport/processors
%{py_sitescriptdir}/bzrlib/plugins/fastimport/processors/*.py[co]
