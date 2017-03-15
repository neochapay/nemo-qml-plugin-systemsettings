Name:       nemo-qml-plugin-systemsettings
Summary:    System settings plugin for Nemo Mobile
Version:    0.2.25
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://git.merproject.org/mer-core/nemo-qml-plugin-systemsettings
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires:       connman
Requires:       mce >= 1.83.0
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5SystemInfo)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(timed-qt5)
BuildRequires:  pkgconfig(profile)
BuildRequires:  pkgconfig(mce)
BuildRequires:  pkgconfig(mlite5)
BuildRequires:  pkgconfig(usb-moded-qt5)
BuildRequires:  pkgconfig(libshadowutils)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(nemomodels-qt5)
BuildRequires:  pkgconfig(libsailfishkeyprovider)

%description
%{summary}.

%package devel
Summary:    System settings C++ library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package tests
Summary:    System settings C++ library (unit tests)
Group:      System/Libraries

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5 
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install
chmod +x %{buildroot}/%{_bindir}/vpn-updown.sh

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/systemsettings/libnemosystemsettings.so
%{_libdir}/qt5/qml/org/nemomobile/systemsettings/qmldir
%{_libdir}/libsystemsettings.so.*
%{_libdir}/systemd/user/vpn-updown.service
%{_bindir}/vpn-updown.sh
%dir %attr(0775, root, privileged) /etc/location
%config %attr(0664, root, privileged) /etc/location/location.conf

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/systemsettings.pc
%{_includedir}/systemsettings/*
%{_libdir}/libsystemsettings.so

%files tests
%defattr(-,root,root,-)
%{_libdir}/%{name}-tests/ut_diskusage
%{_datadir}/%{name}-tests/tests.xml
