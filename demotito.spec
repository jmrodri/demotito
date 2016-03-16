# If on Fedora 12 or RHEL 5 or earlier, we need to define these:
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif


Name: demotito
Version: 0.1.2
Release: 1%{?dist}

Summary: Demo of Tito
Group: Development/Libraries
License: GPLv2
# How to create the source tarball:
#
# git clone git://git.fedorahosted.org/git/python-rhsm.git/
# cd client/python-rhsm
# tito build --tag python-rhsm-$VERSION-$RELEASE --tgz
Source0: %{name}-%{version}.tar.gz
URL: http://github.com/jmrodri/demotito
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A small demo of tito

%prep
%setup -q -n demotito-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_tmppath}
install -m 755 hello.py %{buildroot}%{_tmppath}/hello.py
install -m 755 world.py %{buildroot}%{_tmppath}/world.py

%clean
#rm -rf %{buildroot}

%files
%defattr(755,root,root,755)
%{_tmppath}/hello.py*
%{_tmppath}/world.py*

%changelog
* Wed Mar 16 2016 jesus m. rodriguez <jesusr@redhat.com> 0.1.2-1
- new package built with tito


