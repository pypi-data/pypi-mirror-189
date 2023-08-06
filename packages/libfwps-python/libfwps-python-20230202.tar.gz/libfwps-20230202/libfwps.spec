Name: libfwps
Version: 20230202
Release: 1
Summary: Library to access the Windows Property Store format
Group: System Environment/Libraries
License: LGPLv3+
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libfwps
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
         
BuildRequires: gcc         

%description -n libfwps
Library to access the Windows Property Store format

%package -n libfwps-static
Summary: Library to access the Windows Property Store format
Group: Development/Libraries
Requires: libfwps = %{version}-%{release}

%description -n libfwps-static
Static library version of libfwps.

%package -n libfwps-devel
Summary: Header files and libraries for developing applications for libfwps
Group: Development/Libraries
Requires: libfwps = %{version}-%{release}

%description -n libfwps-devel
Header files and libraries for developing applications for libfwps.

%package -n libfwps-python3
Summary: Python 3 bindings for libfwps
Group: System Environment/Libraries
Requires: libfwps = %{version}-%{release} python3
BuildRequires: python3-devel

%description -n libfwps-python3
Python 3 bindings for libfwps

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libfwps
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.so.*

%files -n libfwps-static
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.a

%files -n libfwps-devel
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfwps.pc
%{_includedir}/*
%{_mandir}/man3/*

%files -n libfwps-python3
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.so

%changelog
* Sat Feb  4 2023 Joachim Metz <joachim.metz@gmail.com> 20230202-1
- Auto-generated

