# spec file for package check_apache_status.pl

%define lname	check_apache_status

Name:          nagios-plugins-apache_status
Summary:       Nagios Plugins - check_apache_status.pl
Version:       1.0.1
Url:           http://github.com/lbetz/nagios-plugins
License:       GPL-2.0+
Group:         System/Monitoring
Source0:       %{lname}-%{version}.tar.gz
Provides:      nagios-plugins-apache_status = %{version}-%{release}
Obsoletes:     nagios-plugins-apache_status < %{version}-%{release}
Requires:      perl(Monitoring::Plugin)
Requires:      perl(LWP::UserAgent)
Requires:      perl(Data::Dumper)

%if 0%{?suse}
Release:       1
BuildRequires: nagios-rpm-macros
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
%endif

%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
Release:       1%{?dist}
Requires:      nagios-common
%endif

%description
Checks against the apache status site.

%prep
%setup -q -n %{lname}-%{version}

%install
%{__mkdir_p} %{buildroot}/%{_libdir}/nagios/plugins
%{__install} -m755 check_apache_status.pl %{buildroot}/%{_libdir}/nagios/plugins/

%clean
rm -rf %buildroot

%files -n nagios-plugins-apache_status
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%if 0%{?suse_version}
%dir %{_libdir}/nagios
%dir %{_libdir}/nagios/plugins
%endif
%{_libdir}/nagios/plugins/check_apache_status.pl

%changelog
* Mon Apr 29 2016 Lennart Betz <lennart.betz@netways.de>
- initial setup