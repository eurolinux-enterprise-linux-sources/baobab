%global gtk3_version 3.13.2

Name:           baobab
Version:        3.14.1
Release:        5%{?dist}
Summary:        A graphical directory tree analyzer

Group:          Applications/System
License:        GPLv2+ and GFDL
URL:            https://live.gnome.org/Baobab
Source0:        http://download.gnome.org/sources/baobab/3.14/%{name}-%{version}.tar.xz

# https://bugzilla.redhat.com/show_bug.cgi?id=1174557
Patch0:         baobab-3.14.2-Translation-updates.patch
Patch1:         baobab-translations-3.14.patch
Patch2:         baobab-3.14.2-Exclude-mountpoints-when-handling-cmd-args.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1233656
Patch3:         baobab-3.14.2-Fix-context-menu-items-sensitivity.patch
Patch4:         baobab-3.14.2-Fix-Zoom-out-item-sensitivity-for-treemap-chart.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=840427
Patch5:         baobab-3.17.90-Exclude-mounts-when-scanning-recent-locations.patch

BuildRequires:  chrpath
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel >= %{gtk3_version}
BuildRequires:  libgtop2-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  vala-tools

Requires: gtk3%{?_isa} >= %{gtk3_version}

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
%patch0 -p1 -b .translation-updates
%patch1 -p1 -b .translation-updates2
%patch2 -p1 -b .exclude-mountpoints
%patch3 -p1
%patch4 -p1
%patch5 -p1 -b .exclude-mountpoints-recent


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/baobab

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.baobab.desktop


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
%{_datadir}/appdata/org.gnome.baobab.appdata.xml
%{_datadir}/applications/org.gnome.baobab.desktop
%{_datadir}/dbus-1/services/org.gnome.baobab.service
%{_datadir}/icons/hicolor/*/apps/baobab.png
%{_datadir}/icons/HighContrast/*/apps/baobab.png
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_mandir}/man1/baobab.1.gz

%changelog
* Fri Sep 11 2015 Ondrej Holy <oholy@redhat.com> - 3.14.1-5
- Exclude mountpoints when scanning recent locations
- Resolves: #840427

* Tue Jul 28 2015 David King <dking@redhat.com> - 3.14.1-4
- Fix menu item sensitivity (#1233656)

* Fri May 15 2015 Ondrej Holy <oholy@redhat.com> - 3.14.1-3
- Exclude mountpoints when handling commandline arguments
- Resolves: #840427

* Fri May 15 2015 Ondrej Holy <oholy@redhat.com> - 3.14.1-2
- Add translation updates from translation team
- Resolves: #1174557

* Tue May 5 2015 Ondrej Holy <oholy@redhat.com> - 3.14.1-1
- Update to 3.14.1
- Remove obsolete upstream patch
- Add translations updates from upstream
- Resolves: #1174557

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
