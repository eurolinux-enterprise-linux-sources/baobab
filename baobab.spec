Name:           baobab
Version:        3.8.2
Release:        4%{?dist}
Summary:        A graphical directory tree analyzer

Group:          Applications/System
License:        GPLv2+ and GFDL
URL:            https://live.gnome.org/Baobab
Source0:        http://download.gnome.org/sources/baobab/3.8/%{name}-%{version}.tar.xz

BuildRequires:  chrpath
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  libgtop2-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  vala-tools

Patch0: baobab-3.8.2_translation_updates.patch

Obsoletes: gnome-utils < 1:3.3
Obsoletes: gnome-utils-devel < 1:3.3
Obsoletes: gnome-utils-libs < 1:3.3

%description
Baobab is able to scan either specific directories or the whole filesystem, in
order to give the user a graphical tree representation including each
directory size or percentage in the branch.  It also auto-detects in real-time
any change made to your home folder as far as any mounted/unmounted device.

%prep
%setup -q
%patch0 -p2 -b .baobab-3.8.2_translation_updates


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/baobab

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/baobab.desktop

%find_lang %{name} --with-gnome


%post
for d in hicolor HighContrast ; do
  touch --no-create %{_datadir}/icons/$d >&/dev/null || :
done


%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas >&/dev/null || :
  for d in hicolor HighContrast ; do
    touch --no-create %{_datadir}/icons/$d >&/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/$d >&/dev/null || :
  done
fi


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas >&/dev/null || :
for d in hicolor HighContrast ; do
  gtk-update-icon-cache %{_datadir}/icons/$d >&/dev/null || :
done


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README COPYING.docs
%{_bindir}/baobab
%{_datadir}/applications/baobab.desktop
%{_datadir}/icons/hicolor/*/apps/baobab.png
%{_datadir}/icons/HighContrast/*/apps/baobab.png
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_mandir}/man1/baobab.1.gz
%{_datadir}/icons/hicolor/scalable/actions/view-ringschart-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/view-treemap-symbolic.svg

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.2-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.2-3
- Mass rebuild 2013-12-27

* Fri Dec 6 2013 Ondrej Holy <oholy@redhat.com> - 3.8.2-2
- Translation updates (#1030317)

* Mon May 13 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.92-1
- Update to 3.7.92

* Wed Mar  6 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90
- Install HighContrast icons and update the rpm scriptlets for the icon cache

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Thu Nov 15 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.3-1
- Update to 3.6.3
- Remove an unwanted lib64 rpath

* Wed Nov 14 2012 Tomas Bzatek <tbzatek@redhat.com> - 3.6.2-2
- Fix homepage URL

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence glib-compile-schemas output

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.4-1
- Update to 3.3.4

* Sat Mar 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-3
- Don't obsolete gnome-system-log

* Fri Mar 16 2012 Rui Matos <rmatos@redhat.com> - 3.3.3-2
- Obsolete all gnome-utils subpackages

* Mon Mar 12 2012 Rui Matos <rmatos@redhat.com> - 3.3.3-1
- Update to 3.3.3
- Just list %%{_datadir}/help/xx_YY/baobab in %%files since %%find_lang
  doesn't find those for us

* Mon Mar  5 2012 Rui Matos <rmatos@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Tue Dec 27 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Initial packaging
